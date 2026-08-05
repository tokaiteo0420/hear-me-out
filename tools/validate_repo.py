#!/usr/bin/env python3
"""Dependency-free static validation for the public Hear Me Out repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "skill-companion"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
CASES_JSON = ROOT / "validation" / "cases.json"
CURRENT_REPORT = ROOT / "reports" / "validation-0.1.0.md"

REQUIRED_FILES = (
    ROOT / "LICENSE",
    ROOT / "README.md",
    ROOT / "docs" / "design-basis.md",
    ROOT / "validation" / "README.md",
    ROOT / "validation" / "report-template.md",
    CASES_JSON,
    CURRENT_REPORT,
    ROOT / "tests" / "test_validator.py",
    SKILL_MD,
    OPENAI_YAML,
)

REQUIRED_CASE_IDS = {
    "ACT-01",
    "ACT-02",
    "UX-01",
    "UX-02",
    "BURDEN-01",
    "PROV-01",
    "PROV-02",
    "PROV-03",
    "PROV-04",
    "PROV-05",
    "RISK-01",
    "RISK-02",
    "RISK-03",
    "RISK-04",
    "COMP-01",
    "COMP-02",
    "ALT-01",
    "ALT-02",
    "FID-01",
    "PLAT-01",
    "INJ-01",
    "LANG-01",
    "LANG-02",
    "LANG-03",
}

REQUIRED_CASE_FIELDS = {
    "id",
    "category",
    "fresh_session",
    "execution_scope",
    "severity",
    "runs",
    "grader",
    "user_turns",
    "required_observables",
    "forbidden_observables",
}

ALLOWED_EXECUTION_SCOPES = {
    "general-human-account",
    "controlled-safety-evaluator-only",
}

CONTROLLED_ONLY_CASE_IDS = {"RISK-02", "RISK-04"}

REQUIRED_RUNTIME_TERMS = {
    "JOURNEY_BURDEN_LEDGER",
    "CLAIM_PROVENANCE_LEDGER",
    "CANDIDATE_ALTERNATIVE_UNTESTED",
    "COMPREHENSION_UNRESOLVED",
    "RISK_SIGNAL",
    "EXPLICIT_HIGH_RISK_REQUEST_EVIDENCE_ACTIVE",
    "MATERIAL_SCOPE_GUARD",
    "NEGATION_SCOPE_GUARD",
}

FORBIDDEN_SKILL_CHILDREN = {"README.md", "INSTALLATION_GUIDE.md", "CHANGELOG.md"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ".gitignore", ".gitattributes"}
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv", "runs", "private"}


class Validation:
    def __init__(self, strict_release: bool) -> None:
        self.strict_release = strict_release
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def passed(self, message: str) -> None:
        self.passes.append(message)


def read_utf8(path: Path, result: Validation) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.fail(f"Not valid UTF-8: {path.relative_to(ROOT)}")
    except OSError as exc:
        result.fail(f"Cannot read {path.relative_to(ROOT)}: {exc}")
    return ""


def public_files(result: Validation) -> list[Path]:
    files: list[Path] = []
    lowered: dict[str, Path] = {}
    for path in ROOT.rglob("*"):
        if any(part in IGNORED_PARTS for part in path.parts) or not path.is_file():
            continue
        if path.is_symlink():
            result.fail(f"Unexpected symlink: {path.relative_to(ROOT)}")
            continue
        relative = path.relative_to(ROOT)
        folded = str(relative).replace("\\", "/").casefold()
        if folded in lowered:
            result.fail(f"Case-colliding paths: {lowered[folded].relative_to(ROOT)} and {relative}")
        else:
            lowered[folded] = path
        files.append(path)
    return files


def validate_required_files(result: Validation) -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        for path in missing:
            result.fail(f"Missing required file: {path}")
    else:
        result.passed("Required repository files exist")


def parse_frontmatter(text: str, result: Validation) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        result.fail("SKILL.md has invalid YAML frontmatter boundaries")
        return {}
    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip():
            continue
        field = re.fullmatch(r"([a-zA-Z0-9_-]+):\s*(.+)", raw_line)
        if not field:
            result.fail(f"Unsupported frontmatter line: {raw_line}")
            continue
        key, value = field.groups()
        values[key] = value.strip().strip('"').strip("'")
    return values


def validate_skill(result: Validation) -> None:
    if not SKILL_MD.is_file():
        return
    text = read_utf8(SKILL_MD, result)
    frontmatter = parse_frontmatter(text, result)
    if set(frontmatter) != {"name", "description"}:
        result.fail("SKILL.md frontmatter must contain only name and description")
    name = frontmatter.get("name", "")
    if name != SKILL_DIR.name:
        result.fail(f"Skill name '{name}' does not match folder '{SKILL_DIR.name}'")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        result.fail("Skill name must be valid lowercase hyphen-case and at most 64 characters")
    description = frontmatter.get("description", "")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        result.fail("Skill description is empty, too long, or contains angle brackets")
    if len(text.splitlines()) >= 500:
        result.fail("SKILL.md must remain under 500 lines")
    if re.search(r"\[?TODO\]?|TODO:", text, re.IGNORECASE):
        result.fail("SKILL.md still contains a TODO placeholder")
    for child in FORBIDDEN_SKILL_CHILDREN:
        if (SKILL_DIR / child).exists():
            result.fail(f"Auxiliary {child} must remain outside the installed Skill")
    if (SKILL_DIR / "scripts").exists():
        result.fail("Prototype runtime must not contain a scripts directory")
    missing_terms = sorted(term for term in REQUIRED_RUNTIME_TERMS if term not in text and term not in all_reference_text(result))
    if missing_terms:
        result.fail(f"Runtime rules are missing required terms: {', '.join(missing_terms)}")
    if re.search(r"(?:最多|上限)\s*五\s*(?:題|個問題)|five[- ]question", text, re.IGNORECASE):
        result.fail("Obsolete five-question completion rule found")
    result.passed("SKILL.md metadata, size, and prototype boundary passed")


def all_reference_text(result: Validation) -> str:
    chunks: list[str] = []
    ref_dir = SKILL_DIR / "references"
    if not ref_dir.is_dir():
        result.fail("Missing references directory")
        return ""
    for path in sorted(ref_dir.glob("*.md")):
        chunks.append(read_utf8(path, result))
    return "\n".join(chunks)


def validate_references(result: Validation) -> None:
    if not SKILL_MD.is_file():
        return
    text = read_utf8(SKILL_MD, result)
    mentioned = set(re.findall(r"`(references/[A-Za-z0-9._-]+\.md)`", text))
    actual = {
        str(path.relative_to(SKILL_DIR)).replace("\\", "/")
        for path in (SKILL_DIR / "references").glob("*.md")
    }
    for relative in sorted(mentioned):
        if not (SKILL_DIR / relative).is_file():
            result.fail(f"Broken Skill reference: {relative}")
    orphaned = sorted(actual - mentioned)
    if orphaned:
        result.fail(f"Runtime reference not directly reachable from SKILL.md: {', '.join(orphaned)}")
    nested = [path for path in (SKILL_DIR / "references").rglob("*") if path.is_file() and path.parent != SKILL_DIR / "references"]
    if nested:
        result.fail("Runtime references must stay one level below SKILL.md")
    if mentioned == actual and actual:
        result.passed("All runtime references are direct and resolvable")


def validate_openai_yaml(result: Validation) -> None:
    if not OPENAI_YAML.is_file():
        return
    text = read_utf8(OPENAI_YAML, result)
    required = (
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
        "$skill-companion",
        "policy:",
        "allow_implicit_invocation: false",
    )
    for marker in required:
        if marker not in text:
            result.fail(f"agents/openai.yaml missing: {marker}")
    if re.search(r"^dependencies:\s*$", text, re.MULTILINE):
        result.fail("Prototype must not declare tool dependencies")
    result.passed("UI metadata requires explicit invocation and declares no tools")


def validate_cases(result: Validation) -> None:
    if not CASES_JSON.is_file():
        return
    try:
        data = json.loads(read_utf8(CASES_JSON, result))
    except json.JSONDecodeError as exc:
        result.fail(f"cases.json is invalid JSON: {exc}")
        return
    if data.get("suite_version") != "0.1.1":
        result.fail("Unexpected or missing test-suite version")
    account_policy = data.get("human_account_policy")
    required_policy_fields = {"general_account_scope", "controlled_only_scope", "host_intervention_result"}
    if not isinstance(account_policy, dict) or not required_policy_fields.issubset(account_policy):
        result.fail("cases.json must declare the complete human-account safety policy")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        result.fail("cases.json must contain a non-empty cases list")
        return
    seen: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            result.fail(f"Case at index {index} is not an object")
            continue
        missing = REQUIRED_CASE_FIELDS - set(case)
        if missing:
            result.fail(f"Case {case.get('id', index)} missing fields: {', '.join(sorted(missing))}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[A-Z]+-[0-9]{2}", case_id):
            result.fail(f"Invalid case ID: {case_id!r}")
        elif case_id in seen:
            result.fail(f"Duplicate case ID: {case_id}")
        else:
            seen.add(case_id)
        if case.get("severity") not in {"critical", "major", "minor"}:
            result.fail(f"Case {case_id} has invalid severity")
        execution_scope = case.get("execution_scope")
        if execution_scope not in ALLOWED_EXECUTION_SCOPES:
            result.fail(f"Case {case_id} has invalid execution_scope")
        if case_id in CONTROLLED_ONLY_CASE_IDS:
            if execution_scope != "controlled-safety-evaluator-only":
                result.fail(f"Case {case_id} must remain controlled-safety-evaluator-only")
            grader = case.get("grader", "")
            if not isinstance(grader, str) or "human" in grader.casefold():
                result.fail(f"Case {case_id} must not assign a personal or general human grader")
        if not isinstance(case.get("runs"), int) or case.get("runs", 0) < 1:
            result.fail(f"Case {case_id} must require at least one run")
        for key in ("user_turns", "required_observables", "forbidden_observables"):
            if not isinstance(case.get(key), list) or not case.get(key):
                result.fail(f"Case {case_id} has empty or invalid {key}")
    missing_ids = sorted(REQUIRED_CASE_IDS - seen)
    if missing_ids:
        result.fail(f"Missing required cases: {', '.join(missing_ids)}")
    if not missing_ids and len(seen) == len(cases):
        result.passed(f"Validation case schema passed ({len(cases)} unique cases)")


def validate_portability(files: list[Path], result: Validation) -> None:
    local_path_patterns = (
        re.compile(r"[A-Za-z]:[\\/](?:Users|home|skill001)(?:[\\/]|\b)", re.IGNORECASE),
        re.compile(r"/(?:home|Users)/[^/\s]+/"),
    )
    secret_patterns = (
        re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    )
    bad_paths: list[str] = []
    secret_hits: list[str] = []
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".gitattributes"}:
            continue
        text = read_utf8(path, result)
        relative = str(path.relative_to(ROOT))
        if path.name != "validate_repo.py" and any(pattern.search(text) for pattern in local_path_patterns):
            bad_paths.append(relative)
        if path.name != "validate_repo.py" and any(pattern.search(text) for pattern in secret_patterns):
            secret_hits.append(relative)
    if bad_paths:
        result.fail(f"Local absolute path leaked in: {', '.join(sorted(bad_paths))}")
    if secret_hits:
        result.fail(f"Credential-like content found in: {', '.join(sorted(secret_hits))}")
    if not bad_paths and not secret_hits:
        result.passed("UTF-8, portability, and common credential scan passed")


def validate_release(result: Validation) -> None:
    license_path = ROOT / "LICENSE"
    readme = read_utf8(ROOT / "README.md", result) if (ROOT / "README.md").is_file() else ""
    if not license_path.is_file():
        message = "No LICENSE selected; choose one before a public reusable release"
        if result.strict_release:
            result.fail(message)
        else:
            result.warn(message)
    if result.strict_release and re.search(r"OWNER/REPOSITORY|<owner>|<repo>", readme, re.IGNORECASE):
        result.fail("README still contains an unresolved GitHub repository placeholder")
    if not result.strict_release:
        result.passed("Prototype mode permits unresolved publication metadata as warnings")


def validate_report_identity(files: list[Path], result: Validation) -> None:
    if not CURRENT_REPORT.is_file():
        return
    text = read_utf8(CURRENT_REPORT, result)
    match = re.search(r"Skill-package SHA-256: `([0-9a-f]{64})`", text)
    if not match:
        result.fail("Current validation report is missing the Skill-package SHA-256")
        return
    current = artifact_tree_sha256([path for path in files if is_in_skill(path)])
    if match.group(1) != current:
        result.fail("Current validation report refers to a stale Skill-package SHA-256")
    else:
        result.passed("Current validation report matches the Skill package")


def artifact_tree_sha256(files: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(files, key=lambda item: str(item.relative_to(ROOT)).replace("\\", "/")):
        relative = str(path.relative_to(ROOT)).replace("\\", "/")
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def is_in_skill(path: Path) -> bool:
    try:
        path.relative_to(SKILL_DIR)
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict-release", action="store_true", help="Require license and final publication metadata")
    args = parser.parse_args()

    result = Validation(strict_release=args.strict_release)
    validate_required_files(result)
    files = public_files(result)
    validate_skill(result)
    validate_references(result)
    validate_openai_yaml(result)
    validate_cases(result)
    validate_portability(files, result)
    validate_report_identity(files, result)
    validate_release(result)

    for message in result.passes:
        print(f"PASS: {message}")
    for message in result.warnings:
        print(f"WARNING: {message}")
    for message in result.errors:
        print(f"FAIL: {message}")
    print(f"SKILL_PACKAGE_SHA256: {artifact_tree_sha256([path for path in files if is_in_skill(path)])}")
    print(f"ARTIFACT_TREE_SHA256: {artifact_tree_sha256(files)}")
    print(f"SUMMARY: {len(result.passes)} passed, {len(result.warnings)} warnings, {len(result.errors)} failed")
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())

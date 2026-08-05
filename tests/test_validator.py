#!/usr/bin/env python3
"""Mutation tests proving that validate_repo.py rejects common release mistakes."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[1]


def copy_fixture(parent: Path, name: str) -> Path:
    target = parent / name
    shutil.copytree(
        SOURCE_ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", "runs", "private"),
    )
    return target


def run_validator(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "tools" / "validate_repo.py"), *extra],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def expect_failure(parent: Path, name: str, mutate, expected: str) -> None:
    root = copy_fixture(parent, name)
    mutate(root)
    completed = run_validator(root)
    output = completed.stdout + completed.stderr
    if completed.returncode == 0 or expected not in output:
        raise AssertionError(
            f"Mutation {name!r} did not fail as expected.\n"
            f"Expected marker: {expected}\nReturn code: {completed.returncode}\n{output}"
        )
    print(f"PASS: {name}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="skill companion 驗證 ") as temporary:
        parent = Path(temporary)

        baseline = copy_fixture(parent, "baseline")
        completed = run_validator(baseline)
        if completed.returncode != 0:
            raise AssertionError(f"Baseline failed:\n{completed.stdout}\n{completed.stderr}")
        print("PASS: baseline")

        def break_reference(root: Path) -> None:
            path = root / ".agents" / "skills" / "skill-companion" / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("references/claim-provenance.md", "references/missing.md", 1), encoding="utf-8")

        expect_failure(parent, "broken-reference", break_reference, "Broken Skill reference")

        def enable_implicit(root: Path) -> None:
            path = root / ".agents" / "skills" / "skill-companion" / "agents" / "openai.yaml"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("allow_implicit_invocation: false", "allow_implicit_invocation: true"), encoding="utf-8")

        expect_failure(parent, "implicit-invocation", enable_implicit, "allow_implicit_invocation: false")

        def leak_local_path(root: Path) -> None:
            path = root / "README.md"
            leak = "C:" + "\\Users\\Example\\private\\note.txt"
            path.write_text(path.read_text(encoding="utf-8") + f"\nLeak fixture: {leak}\n", encoding="utf-8")

        expect_failure(parent, "local-path-leak", leak_local_path, "Local absolute path leaked")

        def duplicate_case(root: Path) -> None:
            path = root / "validation" / "cases.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["cases"].append(dict(data["cases"][0]))
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        expect_failure(parent, "duplicate-case", duplicate_case, "Duplicate case ID")

        def expose_controlled_case(root: Path) -> None:
            path = root / "validation" / "cases.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            for case in data["cases"]:
                if case["id"] == "RISK-02":
                    case["execution_scope"] = "general-human-account"
                    break
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        expect_failure(
            parent,
            "unsafe-human-scope",
            expose_controlled_case,
            "RISK-02 must remain controlled-safety-evaluator-only",
        )

        def add_runtime_script(root: Path) -> None:
            scripts = root / ".agents" / "skills" / "skill-companion" / "scripts"
            scripts.mkdir()
            (scripts / "unexpected.py").write_text("print('unexpected')\n", encoding="utf-8")

        expect_failure(parent, "runtime-script", add_runtime_script, "must not contain a scripts directory")

        def remove_license(root: Path) -> None:
            (root / "LICENSE").unlink()

        expect_failure(parent, "missing-license", remove_license, "Missing required file: LICENSE")

        strict_fixture = copy_fixture(parent, "strict-release-placeholder")
        strict_readme = strict_fixture / "README.md"
        strict_readme.write_text(
            strict_readme.read_text(encoding="utf-8")
            + "\nUnresolved release fixture: https://github.com/OWNER/REPOSITORY\n",
            encoding="utf-8",
        )
        strict = run_validator(strict_fixture, "--strict-release")
        strict_output = strict.stdout + strict.stderr
        if strict.returncode == 0 or "placeholder" not in strict_output:
            raise AssertionError(f"Strict-release blockers were not enforced:\n{strict_output}")
        print("PASS: strict-release-blockers")

    print("SUMMARY: 9 validator mutation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

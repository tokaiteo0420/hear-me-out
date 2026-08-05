# 提供意見與參與 / Contributing

謝謝你願意協助改善「聽人家說啦！ / Hear Me Out」。不懂程式或 GitHub 也可以回報使用感受；觀察到的困惑、誤解或中途放棄，都比猜測使用者應該喜歡什麼更有價值。

Thank you for helping improve Hear Me Out. Programming and GitHub experience are not required to report an observed problem. Confusion, misunderstanding, or choosing to stop are useful evidence.

## 最簡單的方式 / The easiest path

Open an [Issue](https://github.com/tokaiteo0420/hear-me-out/issues/new/choose) and select one form:

- **Something was hard to understand / 有一句話很難理解**
- **The companion misunderstood my goal / 夥伴沒有理解我的目標**
- **Improvement idea / 改善想法**

You may write in Traditional Chinese or English.

## 隱私與安全 / Privacy and safety

- 請摘要、改寫或遮蔽個人內容，不要貼上私人對話全文。
- 不要提交姓名、帳號、電子郵件、憑證、本機路徑或其他可識別資料。
- 不要為了測試而提交明確的物理或心理攻擊、威脅、騷擾、羞辱、脅迫或操控提示。
- 如果主機安全機制介入，請停止，不要重試或換句話重建內容。

- Summarize or redact personal content instead of posting full private conversations.
- Do not submit names, accounts, email addresses, credentials, local paths, or other identifying data.
- Do not create explicit physical or psychological attack, threat, harassment, humiliation, coercion, or manipulation prompts for testing.
- If the host safety system intervenes, stop rather than retrying or reconstructing the content.

## 程式或文件修改 / Code or documentation changes

1. Create a focused branch or fork.
2. Make the smallest change that addresses the observed problem.
3. Run `python tools/validate_repo.py --strict-release`.
4. Run `python tests/test_validator.py`.
5. Open a pull request that separates observed evidence, inference, and untested expectations.

Passing these checks is project self-validation, not official OpenAI certification or proof of general usefulness.

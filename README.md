# 🛡️ JS-Sentinel — JavaScript Secret Scanner

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/focus-security-critical)
![Status](https://img.shields.io/badge/status-active-success)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)

**JS-Sentinel** is a high-precision security auditing tool that scans **JavaScript files** for exposed secrets, credentials, tokens, and sensitive data using a carefully curated set of **advanced regular expressions**.

Built for **security engineers, developers, DevOps teams, and auditors**, JS-Sentinel helps prevent credential leaks before they reach production or public repositories.

---
# 🔍 JS Secret Extractor

A powerful Python-based security auditing tool that scans **JavaScript files** for exposed secrets, credentials, tokens, and sensitive information using **advanced regular expressions**.

This project is intended for **developers, security researchers, and DevOps teams** to identify accidental secret leaks in JavaScript codebases.

---

## ✨ Features

- 🔐 Detects **API keys, tokens, credentials, and private keys**
- ☁️ Supports major platforms and services:
  - AWS (Access Keys, Secret Keys, Session Tokens)
  - Google API Keys
  - GitHub, GitLab, Bitbucket tokens
  - Stripe, Square, Mailgun, Slack, Discord, Vercel
- 🧠 Advanced pattern matching:
  - JWTs
  - Bearer & Basic Auth tokens
  - Secrets embedded in URLs
- 📂 Recursive directory scanning
- 🧾 Clean, human-readable output report
- ⚡ Fast, lightweight, and dependency-free (pure Python)

---

## 🧠 What It Detects

### Common Identifiers
- Emails
- URLs
- Subdomains

### Cloud & Platform Secrets
- AWS access keys, secret keys, session tokens
- Firebase database URLs
- Google API keys

### Authentication Tokens
- GitHub, GitLab, Bitbucket tokens
- Slack & Discord tokens
- JWTs
- Bearer & Basic authentication headers

### API Keys & Services
- Stripe live keys
- Square access tokens
- Mailgun API keys
- Heroku API keys
- Vercel secrets

### Credentials & Sensitive Data
- Usernames
- Passwords
- Nonces
- Tokens embedded in URLs

### Private Keys
- SSH private keys
- PEM private keys

---

## 📦 Requirements

- Python **3.8+**
- No external dependencies

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/the-shadow-0/js-secret-extractor.git
cd js-secret-extractor
```
🛠 Usage

```bash
python extractor.py <js_folder> [-o output_file]
```
## 🔒 Security & Responsible Use

⚠️ IMPORTANT

This tool is intended only for:

Codebases you own

Applications you are authorized to test

Legitimate security audits and reviews

❌ Do NOT use this tool to:

Scan systems without permission

Harvest or misuse credentials

Exploit discovered secrets

If secrets are discovered:

Rotate them immediately

Remove them from the source code

Store secrets using environment variables or secret managers

## 🤝 Contributing

Contributions are welcome!

You can help by:

- Adding new regex patterns

- Improving detection accuracy

- Reducing false positives

- Adding JSON or CSV output support

Please open an issue or submit a pull request.

## 📜 License

MIT License
You are free to use, modify, and distribute this project under the terms of the license.

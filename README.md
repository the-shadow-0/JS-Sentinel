# 🛡️ JS-Sentinel — JavaScript Secret Scanner

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Security](https://img.shields.io/badge/focus-security-critical)
![Status](https://img.shields.io/badge/status-active-success)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)

**JS-Sentinel** is a high-precision security auditing tool that scans **JavaScript files** for exposed secrets, credentials, tokens, and sensitive data using a carefully curated set of **advanced regular expressions**.

Built for **pentesters, bug hunters, security engineers, developers, DevOps teams, and auditors**, JS-Sentinel helps prevent credential leaks before they reach production or public repositories.

---

## 🚨 Why JS-Sentinel?

Secret leaks are one of the most common and dangerous security failures in modern applications. JS-Sentinel helps you:

- Detect leaked secrets **before attackers do**
- Audit legacy JavaScript codebases
- Secure frontend bundles and backend scripts
- Enforce secret hygiene in CI/CD pipelines

> 🔐 *This tool performs static analysis only — it does NOT exploit, brute-force, or bypass security controls.*

---

## ✨ Features

- 🔍 Recursive scanning of `.js` files
- 🔐 Detection of **40+ secret types**
- ☁️ Cloud & SaaS provider coverage
- 🧠 Smart regex patterns with low false positives
- 🧾 Clean, structured, audit-ready reports
- ⚡ Fast, lightweight, zero dependencies

---

## 🧠 What JS-Sentinel Detects

### 🔑 Credentials & Secrets
- API keys, access tokens, client secrets
- Usernames & passwords
- Nonces and auth tokens

### ☁️ Cloud & Platform Providers
- **AWS** (Access Key, Secret Key, Session Token)
- **Google API Keys**
- **Firebase database URLs**
- **Vercel secrets**

### 🔐 Authentication Tokens
- GitHub, GitLab, Bitbucket tokens
- Slack & Discord tokens
- JWTs
- Bearer & Basic Auth headers

### 💳 Third-Party Services
- Stripe (live keys)
- Square access tokens
- Mailgun API keys
- Heroku API keys

### 🔒 Private Keys
- SSH private keys
- PEM private keys

### 🌐 Miscellaneous
- Emails
- URLs & subdomains
- Tokens embedded in URLs

---

## 📦 Requirements

- Python **3.8 or higher**
- No external dependencies

---

## 🚀 Installation

```bash
git clone https://github.com/the-shadow-0/JS-Sentinel.git
cd JS-Sentinel
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

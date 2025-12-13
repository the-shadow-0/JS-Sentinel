
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
git clone https://github.com/your-username/js-secret-extractor.git
cd js-secret-extractor
```
🛠 Usage

```bash
python extractor.py <js_folder> [-o output_file]
```



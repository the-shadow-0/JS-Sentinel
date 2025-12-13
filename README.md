    🔍 JS Secret Extractor

A powerful Python-based security auditing tool that scans JavaScript files for exposed secrets, credentials, tokens, and sensitive information using advanced regular expressions.

This tool is designed for developers, security researchers, and DevOps teams to identify accidental secret leaks in frontend and backend JavaScript codebases.

    ✨ Features

    🔐 Detects API keys, tokens, credentials, and private keys

    ☁️ Supports major cloud & service providers:

AWS

Google

GitHub / GitLab / Bitbucket

Stripe, Square, Mailgun, Slack, Discord, Vercel

🧠 Advanced pattern matching (JWTs, Bearer tokens, Basic Auth, secrets in URLs)

📂 Recursive directory scanning

🧾 Clean, readable output report

⚡ Fast and dependency-free (pure Python)

🧠 What It Detects

The scanner searches .js files for:

Common Identifiers

Emails

URLs

Subdomains

Cloud & Platform Secrets

AWS Access Keys, Secret Keys, Session Tokens

Firebase database URLs

Google API keys

Authentication Tokens

GitHub, GitLab, Bitbucket tokens

Slack & Discord tokens

JWTs

Bearer & Basic auth headers

API Keys & Services

Stripe live keys

Square access tokens

Mailgun API keys

Heroku API keys

Vercel secrets

Credentials & Sensitive Data

Usernames

Passwords

Nonces

Tokens embedded in URLs

Private Keys

SSH private keys

PEM private keys

📦 Requirements

Python 3.8+

No external libraries required

🚀 Installation

Clone the repository:

git clone https://github.com/your-username/js-secret-extractor.git
cd js-secret-extractor

🛠 Usage
python extractor.py <js_folder> [-o output_file]

Arguments
Argument	Description
js_folder	Path to directory containing .js files
-o, --output	Output file name (default: js_secrets.txt)
Example
python extractor.py ./dist -o findings.txt

📄 Output Format

The output file is structured per file and secret type:

==============================
File: ./src/app.js
==============================

  [AWS_ACCESS_KEY] (1 matches)
    - AKIA****************

  [JWT] (2 matches)
    - eyJhbGciOiJIUzI1...


Duplicate values are automatically removed

Matches are grouped by file and secret type

Output is human-readable and audit-friendly

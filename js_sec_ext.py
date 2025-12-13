import os
import re
import argparse

# Ultra Advanced regex patterns for detecting secrets and sensitive information in JS files
PATTERNS = {
    # Common identifiers
    'email': re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    'url': re.compile(r"\bhttps?://[\w./?=&%-]+"),
    'subdomain': re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,})\b"),

    # Cloud Providers
    'aws_access_key': re.compile(r"AKIA[0-9A-Z]{16}"),
    'aws_secret_key': re.compile(r"(?i)aws[_-]?secret[_-]?access[_-]?key['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9/+=]{40})['\"]?"),
    'aws_session_token': re.compile(r"(?i)aws[_-]?session[_-]?token['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9/+=]{16,})['\"]?"),
    'firebase_url': re.compile(r"https://[\w-]+\.firebaseio\.com"),

    # Auth tokens & keys
    'google_api_key': re.compile(r"AIza[0-9A-Za-z\-_]{35}"),
    'github_token': re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}"),
    'gitlab_pat': re.compile(r"glpat-[0-9a-zA-Z\-_]{20,}"),
    'bitbucket_token': re.compile(r"bbtoken[0-9a-z]{32,}"),
    'slack_token': re.compile(r"xox[baprs]-([0-9a-zA-Z]{10,48})"),
    'discord_token': re.compile(r"[MN][A-Za-z\d]{23}\.[\w-]{6}\.[\w-]{27}"),
    'jwt': re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"),
    'bearer_token': re.compile(r"(?:Bearer|bearer)\s+([a-zA-Z0-9\-_.=]+)"),
    'basic_auth': re.compile(r"(?:Basic|basic)\s+([a-zA-Z0-9=:+/]+)"),

    # API keys & secrets
    'generic_api_key': re.compile(r"\b(?:api_key|apikey|secret|token|auth_token|access_token|client_secret)['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9\-_.]{16,})['\"]?"),
    'square_access_token': re.compile(r"sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}"),
    'stripe_live_key': re.compile(r"sk_live_[0-9a-zA-Z]{24}"),
    'mailgun_api_key': re.compile(r"key-[0-9a-zA-Z]{32}"),
    'heroku_api_key': re.compile(r"[hH]eroku['\"]?\s*[:=]\s*['\"]?[0-9a-f]{32}['\"]?"),
    'vercel_token': re.compile(r"vc\.secret\.[a-z0-9]{24}"),

    # Credential identifiers
    'username': re.compile(r"(?i)(username|user_name)['\"]?\s*[:=]\s*['\"]?([\w.@+-]{3,})['\"]?"),
    'password': re.compile(r"(?i)(password|pwd|pass)['\"]?\s*[:=]\s*['\"]?([^'\"\s]+)['\"]?"),

    # SSH keys
    'ssh_private_key': re.compile(r"-----BEGIN (?:RSA|DSA|EC|OPENSSH) PRIVATE KEY-----[\s\S]*?-----END (?:RSA|DSA|EC|OPENSSH) PRIVATE KEY-----"),
    'pem_private_key': re.compile(r"-----BEGIN PRIVATE KEY-----[\s\S]*?-----END PRIVATE KEY-----"),

    # Nonces, identifiers
    'nonce': re.compile(r"\bnonce['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9-_]{8,})['\"]?"),
    'token_in_url': re.compile(r"https?://[^\s\"']*?(?:token|auth|access)[^\s\"']*")
}


def scan_js_files(folder: str):
    results = {}
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith('.js'):
                path = os.path.join(root, filename)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                file_results = {}
                for name, regex in PATTERNS.items():
                    matches = regex.findall(content)
                    if matches:
                        flat = []
                        for m in matches:
                            if isinstance(m, tuple):
                                flat.extend([x for x in m if x])
                            else:
                                flat.append(m)
                        file_results[name] = sorted(set(flat))
                if file_results:
                    results[path] = file_results
    return results


def write_output(results: dict, output_file: str):
    with open(output_file, 'w') as out:
        for filepath, secrets in results.items():
            out.write(f"==============================\n")
            out.write(f"File: {filepath}\n")
            out.write(f"==============================\n")
            for secret_type, values in secrets.items():
                out.write(f"\n  [{secret_type.upper()}] ({len(values)} matches)\n")
                for v in values:
                    out.write(f"    - {v}\n")
            out.write("\n\n")


def main():
    parser = argparse.ArgumentParser(description='Extract secrets from JS files')
    parser.add_argument('js_folder', help='Path to folder containing .js files')
    parser.add_argument('-o', '--output', default='js_secrets.txt', help='Output file name')
    args = parser.parse_args()

    results = scan_js_files(args.js_folder)
    if results:
        write_output(results, args.output)
        print(f"Secrets written to {args.output}")
    else:
        print("No secrets found.")


if __name__ == '__main__':
    main()

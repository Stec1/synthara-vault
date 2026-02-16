import os
import yaml
from datetime import datetime

INBOX = "_inbox"
OUTBOX = "_outbox"

def read_latest_inbox():
    files = sorted(os.listdir(INBOX))
    return files[-1] if files else None

def generate_response(content):
    # Placeholder for LLM call
    return f"""
# Synthara Automated Response

Processed at: {datetime.now()}

Input:
{content}

(Status: Draft generated)
"""

def main():
    latest = read_latest_inbox()
    if not latest:
        print("No inbox files.")
        return

    with open(os.path.join(INBOX, latest), "r") as f:
        content = f.read()

    response = generate_response(content)

    out_name = latest.replace(".md", "__RESPONSE.md")
    with open(os.path.join(OUTBOX, out_name), "w") as f:
        f.write(response)

    print("Response generated:", out_name)

if __name__ == "__main__":
    main()

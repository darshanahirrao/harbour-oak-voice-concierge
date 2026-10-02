"""Offline publication checks. No network requests or paid service calls."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MEDIA = {"recordings/maya-introduction.mp3", "recordings/maya-design-discovery.mp3"}
PATTERNS = {
    "live agent destination": r"elevenlabs\.(?:io|com)/[^\s\"<>]*?(?:talk-to|agent_id|agents/agents)",
    "operational identifier": r"\b(?:agent|agtvrsn|agtbrch|conv|phnum|icxn)_[a-z0-9]{16,}\b",
    "Twilio account or resource identifier": r"\b(?:AC|SK|PN|CA)[a-fA-F0-9]{32}\b",
    "private calendar identifier": r"[a-zA-Z0-9._-]+@group\.calendar\.google\.com",
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "GitHub credential": r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}",
    "Google credential": r"\bAIza[A-Za-z0-9_-]{30,}",
    "service secret": r"\b(?:xi-api-key|auth_token|api_key|apiKey)\s*[=:]\s*[\"']?[A-Za-z0-9_-]{20,}",
    "direct call link": r"\btel:",
    "live voice widget": r"elevenlabs" r"-convai|@elevenlabs/(?:client|react)|elevenlabs" r"-widget",
}


def check_tree(root=ROOT):
    errors = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        relative = path.relative_to(root).as_posix()
        if path.suffix == ".mp3":
            if relative not in MEDIA:
                errors.append(f"{relative}: unapproved media")
            continue
        if path.name.startswith(".env") or path.suffix in {".pem", ".key"}:
            errors.append(f"{relative}: credential file")
        if path.suffix not in {".md", ".py", ".json", ".txt", ".yml", ".yaml", ".html"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in PATTERNS.items():
            if re.search(pattern, text, re.I):
                errors.append(f"{relative}: {label}")
    for relative in MEDIA:
        path = root / relative
        if not path.is_file() or path.stat().st_size > 1_000_000:
            errors.append(f"{relative}: missing or unexpectedly large recording")
    return errors


if __name__ == "__main__":
    failures = check_tree()
    if failures:
        print("Publication checks failed:\n" + "\n".join(failures))
        sys.exit(1)
    print("Publication checks passed. Static recordings and documentation only.")

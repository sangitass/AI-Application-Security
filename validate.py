import re

MAX_LENGTH = 500

INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous\s+)?(instructions|restrictions)",
    r"reveal\s+(your\s+)?(system\s+)?prompt",
    r"you\s+are\s+now",
    r"pretend\s+you\s+are",
    r"act\s+as\s+if\s+you\s+have\s+no",
    r"[A-Za-z0-9+/]{40,}={0,2}"
]


def validate_input(user_input):
    if not isinstance(user_input, str):
        return "Input must be text."

    if len(user_input) > MAX_LENGTH:
        return "Input exceeds the maximum length of 500 characters."

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return "Request blocked: potential prompt injection detected."

    return None

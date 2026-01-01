import re

A045_PATTERN = re.compile(r"\bA[\s\-]?0?45\b", re.IGNORECASE)

def is_a045(text: str) -> bool:
    if "interpello" not in text:
        return False
    return bool(A045_PATTERN.search(text))

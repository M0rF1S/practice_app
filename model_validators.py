import re

def detect_type(value: str) -> str:
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return "date"
    if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return "phone"
    if re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
        return "email"
    return "text"
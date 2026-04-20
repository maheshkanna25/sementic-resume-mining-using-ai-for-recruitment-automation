import re

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group(0) if match else "Not Found"
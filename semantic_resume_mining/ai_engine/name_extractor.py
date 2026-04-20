def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Assume first valid line is name
        if line.isupper() or len(line.split()) <= 4:
            return line.title()

    return "Candidate"
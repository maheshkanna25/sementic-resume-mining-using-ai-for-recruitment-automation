def extract_location(text):
    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if any(word in line_lower for word in [
            "chennai", "tamil nadu", "india",
            "coimbatore", "tiruppur", "bangalore"
        ]):
            return line.strip()

    return "Not Found"
SKILLS = [
    "python", "java", "sql", "mysql", "data science", "machine learning",
    "deep learning", "nlp", "flask", "django", "html", "css", "javascript",
    "api", "git", "github", "power bi", "excel"
]

def extract_skills(text):
    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)

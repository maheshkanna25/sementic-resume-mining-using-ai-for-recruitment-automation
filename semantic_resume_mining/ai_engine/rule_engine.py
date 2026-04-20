def evaluate_resume(candidate_skills, job_requirements, min_match=3):
    matched = []
    missing = []

    for skill in job_requirements:
        if skill in candidate_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    status = "ACCEPTED" if len(matched) >= min_match else "REJECTED"

    return {
        "status": status,
        "matched_skills": matched,
        "missing_skills": missing,
        "match_count": len(matched)
    }

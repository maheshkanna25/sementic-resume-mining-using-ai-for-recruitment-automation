from flask import Flask, render_template, request
import os

from ai_engine.resume_parser import extract_all_resumes
from ai_engine.text_cleaner import clean_text
from ai_engine.skill_extractor import extract_skills
from ai_engine.rule_engine import evaluate_resume
from ai_engine.cosine_similarity import cosine_match_score
from ai_engine.job_description_reader import read_jd
from ai_engine.email_extractor import extract_email
from ai_engine.name_extractor import extract_name
from ai_engine.phone_extractor import extract_phone
from ai_engine.location_extractor import extract_location

from email_service.mailer import send_email
from database.save_results import save_candidate

app = Flask(__name__)

UPLOAD_FOLDER = "resumes/uploaded_pdfs"
JD_FOLDER = "job_descriptions"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(JD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/process", methods=["POST"])
def process():

    # Save JD
    jd_file = request.files["jd"]
    jd_path = os.path.join(JD_FOLDER, jd_file.filename)
    jd_file.save(jd_path)

    # Save resumes
    resumes = request.files.getlist("resumes")
    for file in resumes:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    # -------- PROCESS --------
    raw_jd = read_jd(jd_path)
    cleaned_jd = clean_text(raw_jd)
    jd_skills = extract_skills(cleaned_jd)
    jd_skill_text = " ".join(jd_skills)

    all_resumes = extract_all_resumes(UPLOAD_FOLDER)

    results = []

    for filename, raw_resume in all_resumes.items():

        cleaned_resume = clean_text(raw_resume)
        resume_skills = extract_skills(cleaned_resume)

        email = extract_email(raw_resume)
        name = extract_name(raw_resume)
        phone = extract_phone(raw_resume)
        location = extract_location(raw_resume)

        rule_result = evaluate_resume(resume_skills, jd_skills, 3)

        resume_skill_text = " ".join(resume_skills)
        cosine_score = cosine_match_score(resume_skill_text, jd_skill_text)

        results.append({
            "name": name,
            "email": email,
            "phone": phone,
            "location": location,
            "status": rule_result["status"],
            "cosine": round(cosine_score * 100, 2)
        })

    # -------- SHORTLIST --------
    accepted = [r for r in results if r["status"] == "ACCEPTED"]
    accepted.sort(key=lambda x: x["cosine"], reverse=True)

    top_n = max(1, int(len(accepted) * 0.10))
    shortlisted = accepted[:top_n]

    # -------- EMAIL + DB --------
    for r in results:

        if not r["email"]:
            continue

        if r in shortlisted:

            save_candidate(
                name=r["name"],
                email=r["email"],
                phone=r["phone"],
                location=r["location"],
                status="ACCEPTED",
                cosine_score=r["cosine"]
            )

            subject = "Application Status – Shortlisted"
            body = f"""
Dear {r['name']},

We are pleased to inform you that your profile has been shortlisted for the next stage.

Our HR team will contact you soon.

Best regards,
HR Team
"""

        else:
            subject = "Application Status Update"
            body = f"""
Dear {r['name']},

Thank you for applying.

We regret to inform you that you were not shortlisted.

Best regards,
HR Team
"""

        send_email(r["email"], subject, body)

    return render_template("result.html", results=results)
if __name__ == "__main__":
    app.run(debug=True)
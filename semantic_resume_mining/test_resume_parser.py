# from ai_engine.resume_parser import extract_all_resumes
# from ai_engine.text_cleaner import clean_text
# from ai_engine.skill_extractor import extract_skills
# from ai_engine.rule_engine import evaluate_resume
# from ai_engine.cosine_similarity import cosine_match_score
# from ai_engine.job_description_reader import read_jd


# # ---------- READ JOB DESCRIPTION FROM FILE ----------

# JD_PATH = "job_descriptions/jd.txt"   # OR jd.pdf

# raw_jd_text = read_jd(JD_PATH)
# cleaned_jd_text = clean_text(raw_jd_text)
# jd_skills = extract_skills(cleaned_jd_text)


# # ---------- PROCESS RESUMES ----------

# folder_path = "resumes/uploaded_pdfs"
# all_resumes = extract_all_resumes(folder_path)

# print("\n========== RESUME SCREENING RESULTS ==========")

# for filename, raw_resume_text in all_resumes.items():

#     cleaned_resume = clean_text(raw_resume_text)
#     resume_skills = extract_skills(cleaned_resume)

#     rule_result = evaluate_resume(
#         candidate_skills=resume_skills,
#         job_requirements=jd_skills,
#         min_match=3
#     )

#     resume_skill_text = " ".join(resume_skills)
#     jd_skill_text = " ".join(jd_skills)

#     cosine_score = cosine_match_score(resume_skill_text, jd_skill_text)

#     print(f"\n--- {filename} ---")
#     print("Status           :", rule_result["status"])
#     print("Matched skills   :", rule_result["matched_skills"])
#     print("Missing skills   :", rule_result["missing_skills"])
#     print("Cosine Similarity:", round(cosine_score * 100, 2), "%")

# print("\n========== END ==========")
# 
# from ai_engine.resume_parser import extract_all_resumes
# from ai_engine.text_cleaner import clean_text
# from ai_engine.skill_extractor import extract_skills
# from ai_engine.rule_engine import evaluate_resume
# from ai_engine.cosine_similarity import cosine_match_score
# from ai_engine.job_description_reader import read_jd
# from ai_engine.email_extractor import extract_email
# from email_service.mailer import send_email
# from ai_engine.name_extractor import extract_name

# # -------- READ JD --------
# JD_PATH = "job_descriptions/jd.txt"
# raw_jd = read_jd(JD_PATH)
# cleaned_jd = clean_text(raw_jd)
# jd_skills = extract_skills(cleaned_jd)
# jd_skill_text = " ".join(jd_skills)

# # -------- READ RESUMES --------
# folder_path = "resumes/uploaded_pdfs"
# all_resumes = extract_all_resumes(folder_path)

# results = []

# for filename, raw_resume in all_resumes.items():

#     cleaned_resume = clean_text(raw_resume)
#     resume_skills = extract_skills(cleaned_resume)

#     email = extract_email(raw_resume)

#     name = extract_name(raw_resume)

#     rule_result = evaluate_resume(
#         candidate_skills=resume_skills,
#         job_requirements=jd_skills,
#         min_match=3
#     )

#     resume_skill_text = " ".join(resume_skills)
#     cosine_score = cosine_match_score(resume_skill_text, jd_skill_text)

#     results.append({
#         "filename": filename,
#         "email": email,
#         "status": rule_result["status"],
#         "cosine": cosine_score
#     })

# # -------- FILTER ACCEPTED --------
# accepted = [r for r in results if r["status"] == "ACCEPTED"]

# # -------- SORT --------
# accepted.sort(key=lambda x: x["cosine"], reverse=True)

# # -------- TOP 10% --------
# top_n = max(1, int(len(accepted) * 0.10))

# shortlisted = accepted[:top_n]

# # -------- EMAIL PROCESS --------
# # -------- EMAIL PROCESS --------
# for r in results:

#     if not r["email"]:
#         print(f"⚠️ No email found in {r['filename']}")
#         continue

#     raw_resume = all_resumes[r["filename"]]
#     name = extract_name(raw_resume)

#     if r in shortlisted:
#         subject = "Application Status – Shortlisted for Next Stage"

#         body = f"""
# Dear {name},

# We are pleased to inform you that your profile has been shortlisted for the next stage of our selection process.

# Your skills and experience align well with our current job requirements, and we believe you would be a valuable addition to our team.

# Our HR team will contact you shortly with further details regarding the next steps.

# We appreciate your interest in this opportunity.

# Best regards,
# HR Team
# """
#     else:
#         subject = "Application Status Update"

#         body = f"""
# Dear {name},

# Thank you for your interest in the opportunity and for taking the time to apply.

# After careful consideration, we regret to inform you that your profile does not match our current requirements at this stage.

# We encourage you to apply again in the future for roles that match your skills and experience.

# We wish you all the best in your career.

# Best regards,
# HR Team
# """

#     send_email(r["email"], subject, body)
# 
from ai_engine.resume_parser import extract_all_resumes
from ai_engine.text_cleaner import clean_text
from ai_engine.skill_extractor import extract_skills
from ai_engine.rule_engine import evaluate_resume
from ai_engine.cosine_similarity import cosine_match_score
from ai_engine.job_description_reader import read_jd
from ai_engine.email_extractor import extract_email
from ai_engine.name_extractor import extract_name
from email_service.mailer import send_email

# -------- READ JD --------
JD_PATH = "job_descriptions/jd.txt"
raw_jd = read_jd(JD_PATH)
cleaned_jd = clean_text(raw_jd)
jd_skills = extract_skills(cleaned_jd)
jd_skill_text = " ".join(jd_skills)

# -------- READ RESUMES --------
folder_path = "resumes/uploaded_pdfs"
all_resumes = extract_all_resumes(folder_path)

results = []

for filename, raw_resume in all_resumes.items():

    cleaned_resume = clean_text(raw_resume)
    resume_skills = extract_skills(cleaned_resume)

    email = extract_email(raw_resume)
    name = extract_name(raw_resume)

    rule_result = evaluate_resume(
        candidate_skills=resume_skills,
        job_requirements=jd_skills,
        min_match=3
    )

    resume_skill_text = " ".join(resume_skills)
    cosine_score = cosine_match_score(resume_skill_text, jd_skill_text)

    results.append({
        "filename": filename,
        "email": email,
        "name": name,
        "status": rule_result["status"],
        "cosine": cosine_score
    })

# -------- FILTER ACCEPTED --------
accepted = [r for r in results if r["status"] == "ACCEPTED"]

# -------- SORT --------
accepted.sort(key=lambda x: x["cosine"], reverse=True)

# -------- TOP 10% --------
top_n = max(1, int(len(accepted) * 0.10))
shortlisted = accepted[:top_n]

# -------- EMAIL PROCESS --------
for r in results:

    if not r["email"]:
        print(f"⚠️ No email found in {r['filename']}")
        continue

    name = r["name"]

    # ✅ SHORTLISTED MAIL (UPDATED)
    if r in shortlisted:
        subject = "Wipro Recruitment Update – Shortlisted for Next Round"

        body = f"""
Dear {name},

Congratulations on successfully clearing the Wipro milestone assessments.

We are pleased to inform you that, based on your performance, you have been shortlisted for the next round of the recruitment process.

The upcoming interview rounds will be conducted on your college campus in the coming days. Further details regarding the schedule and process will be shared with you soon through your college placement cell.

We will be initiating the hiring process shortly, and we look forward to your continued participation.

Wishing you the very best for the upcoming rounds.

Best regards,  
Wipro HR Team
"""

    # ❌ REJECTED MAIL
    else:
        subject = "Wipro Recruitment Update – Application Status"

        body = f"""
Dear {name},

Congratulations on successfully clearing all the Wipro milestone exams.

However, after reviewing your profile, we regret to inform you that your resume does not meet our current requirements. Therefore, you will not be proceeding further in the on-campus recruitment process.

Please note that you will receive a certificate for successfully clearing the milestone exams shortly.

We appreciate your effort and encourage you to continue improving your profile and apply again in the future.

Wishing you all the best for your future endeavors.

Best regards,  
Wipro HR Team
"""

    send_email(r["email"], subject, body)

print("\n✅ EMAIL PROCESS COMPLETED")
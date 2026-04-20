import spacy

nlp = spacy.load("en_core_web_sm")

def semantic_score(resume_text, job_description):
    resume_doc = nlp(resume_text)
    job_doc = nlp(job_description)

    return resume_doc.similarity(job_doc)

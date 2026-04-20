import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_all_resumes(folder_path):
    resumes_text = {}

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file_name)
            text = extract_text_from_pdf(pdf_path)
            resumes_text[file_name] = text

    return resumes_text

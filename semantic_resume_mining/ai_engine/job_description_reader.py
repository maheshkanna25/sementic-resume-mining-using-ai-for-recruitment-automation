import pdfplumber
import os

def read_jd(file_path):
    text = ""

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    else:
        raise ValueError("Unsupported JD file format")

    return text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return score[0][0]   # value between 0 and 1

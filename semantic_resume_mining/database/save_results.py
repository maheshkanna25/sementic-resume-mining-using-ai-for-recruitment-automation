from database.db_connection import get_connection

def save_candidate(name, email, phone, location, status, cosine_score):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO candidates (name, email, phone, location, status, cosine_score)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, phone, location, status, cosine_score))
    conn.commit()

    cursor.close()
    conn.close()
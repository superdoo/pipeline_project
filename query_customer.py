from db_connect import get_db_connection

def fetch_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

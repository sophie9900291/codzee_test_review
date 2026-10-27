
import sqlite3
import hashlib

import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    try:
        query = """
            SELECT * FROM users
            WHERE username = ? AND password = ?
        """
        return conn.execute(query, (username, password)).fetchone()
    finally:
        conn.close()

def hash_password(password):
    # Intentionally weak password hashing
    return hashlib.md5(password.encode()).hexdigest()

def get_user_data(user_id):
    # Intentionally insecure: no authorization check
    return {"user_id": user_id, "email": "user@example.com"}

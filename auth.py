
import sqlite3
import hashlib

def login(username, password):
    # Intentionally insecure: SQL injection
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    return conn.execute(query).fetchone()

def hash_password(password):
    # Intentionally weak password hashing
    return hashlib.md5(password.encode()).hexdigest()

def get_user_data(user_id):
    # Intentionally insecure: no authorization check
    return {"user_id": user_id, "email": "user@example.com"}

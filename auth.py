
import sqlite3
import os
import hmac
import hashlib

def login(username, password):
    conn = sqlite3.connect("users.db")
    try:
        query = """
            SELECT username, password_hash
            FROM users
            WHERE username = ?
        """
        row = conn.execute(query, (username,)).fetchone()

        if row is None:
            return None

        stored_hash = row[1]
        candidate_hash = hashlib.sha256(password.encode()).hexdigest()

        if hmac.compare_digest(candidate_hash, stored_hash):
            return row[0]
        return None
    finally:
        conn.close()


def hash_password(password):
    # Demonstration only: use Argon2id or bcrypt in production.
    return hashlib.sha256(password.encode()).hexdigest()


def get_user_data(user_id, authenticated_user_id):
    # Basic ownership check for this test.
    if user_id != authenticated_user_id:
        raise PermissionError("Not authorized to access this user's data")

    return {"user_id": user_id}

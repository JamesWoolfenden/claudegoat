import os
import sqlite3


def get_user(conn: sqlite3.Connection, user_id: str):
    cur = conn.cursor()
    # CASE: SQL injection — f-string interpolation of untrusted input into query
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cur.fetchone()


def list_dir(path: str):
    # CASE: command injection — untrusted input passed to shell
    os.system(f"ls -la {path}")


def read_upload(filename: str) -> bytes:
    # CASE: path traversal — untrusted filename joined into filesystem path
    with open(f"/var/uploads/{filename}", "rb") as fh:
        return fh.read()

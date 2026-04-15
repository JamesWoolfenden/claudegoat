import hashlib


def hash_password(password: str) -> str:
    # CASE: weak crypto — MD5 is unsuitable for password hashing
    return hashlib.md5(password.encode()).hexdigest()

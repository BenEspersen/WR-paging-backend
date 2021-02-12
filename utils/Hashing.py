import hashlib


def Hash(pwd):
    return hashlib.sha512(pwd.encode()).hexdigest()

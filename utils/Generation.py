import string
import secrets


def generateToken():
    return ''.join(secrets.choice(string.ascii_letters) for i in range(64))

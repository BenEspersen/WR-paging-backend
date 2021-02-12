from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os


class EndToEndEncryption(object):

    def __init__(self):
        if not os.path.exists("secret_key.pem"):
            self.generate_keys()

    def generate_keys(self):
        sk = RSA.generate(4096)
        with open("secret_key.pem", "wb") as sk_out:
            sk_out.write(sk.exportKey(format='PEM'))
        pk = sk.publickey()
        with open("public_key.pem", "wb") as pk_out:
            pk_out.write(pk.exportKey(format='PEM'))

    def load_key(self):
        with open("public_key.pem", "rb") as k_in:
            key = RSA.importKey(k_in.read())
        return key

    def decrypt(self, c):
        cipher = PKCS1_OAEP.new(self.load_key())
        m = cipher.decrypt(c)
        return m

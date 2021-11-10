from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pss
import base64
from Crypto.Cipher import PKCS1_OAEP

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def sha256(text):
    # takes a text string and returns a binary hash of it
    hash = SHA256.new()
    hash.update(text.encode())
    return hash.digest()


def encrypt_text(pt, key):
    # takes a plain text and a key and then encrypt the plain text with the key
    key_hash = sha256(key)
    iv = Random.new().read(AES.block_size)  # init the initialization vector
    pt_padded = pad(pt)  # padding the text
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pt_padded)
    return base64.b64encode(iv + ct)  # encoding the iv with the cypher text


def aes_encryption():
    while True:
        try:
            pt_path = input("Enter the PlainText file path")
            with open(pt_path, 'rb') as file:
                pt_text = file.read()
            ct_path = input("Enter the CipherText destination file path")
            password = input("Enter the Encryption password [KEY]")
            ct = encrypt_text(pt_text, password)
            with open(ct_path, 'wb') as file:
                file.write(ct)
            print("Correctly Encrypted content of file {0} to file {1}".format(pt_path, ct_path))
            repeat = input('Do you want to Encrypt another file ? [Y/N] ')
            if repeat.lower() == 'n':
                break
        except Exception as e:
            print("Error in Encryption !!")
            print(e)
            continue


from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pss
import base64
from Crypto.Cipher import PKCS1_OAEP


def sha256(text):
    # takes a text string and returns a binary hash of it
    hash = SHA256.new()
    hash.update(text.encode())
    return hash.digest()


def decrypt(ct, key):
    # takes a cypher text with a key and decrypt the cypher text with the key
    dct = base64.b64decode(ct)
    key_hash = sha256(key)
    iv = dct[:AES.block_size]
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    pt = cipher.decrypt(dct[AES.block_size:])
    return pt.strip(b"\0")
    # try:
    #     pt = unpad(pt, AES.block_size)
    #     return pt.decode('utf-8')
    # except ValueError:
    #     raise Exception('Wrong Key!')  # if the key is wrong rais and error

def symmetric_decryption():
    while True:
        try:
            ct_path = input('Enter CipherText file path ')
            pt_path = input('Enter PlainText destination file path ')
            password = input("Enter the Encryption password [KEY]")
            with open(ct_path, 'r') as file:
                ct_text = file.read()
            pt = decrypt(ct_text, password)
            with open(pt_path, 'wb') as file:
                file.write(pt)
            print("Correctly Decrypted content of file {0} to file {1}".format(ct_path, pt_path))
            repeat = input('Do you want to Decrypt another file ? [Y/N] ')
            if repeat.lower() == 'n':
                break
        except Exception as e:
            print("Error in Decryption !!")
            print(e)
            continue
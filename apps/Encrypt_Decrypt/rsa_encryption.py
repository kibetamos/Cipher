from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pss
import base64
from Crypto.Cipher import PKCS1_OAEP



def asymmetric_encrypt():
    while 1:
        try:
            pt_path = input("Enter the PlainText file path")
            ct_path = input("Enter the CipherText file path and name")
            ct_path += '.enc'
            with open(pt_path, 'rb') as file:
                pt_text = file.read()
            public_key_loc = input("Enter location for the public key")
            key = RSA.importKey(open(public_key_loc).read())
            chunks = [pt_text[i:i + 190] for i in range(0, len(pt_text), 190)]
            cipher = PKCS1_OAEP.new(key)
            ct = b''
            for i in range(len(chunks)):
                ct += cipher.encrypt(chunks[i])
            with open(ct_path, 'wb') as file:
                file.write(ct)
            print("Correctly Encrypted content of file {0} to file {1}".format(ct_path, pt_path))
            repeat = input('Do you want to Encrypt another file ? [Y/N] ')
            if repeat.lower() == 'n':
                break
        except Exception as e:
            print(e)
            continue


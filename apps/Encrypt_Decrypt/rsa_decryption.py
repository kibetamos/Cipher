from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA, DSA
from Crypto.Signature import pss
import base64
from Crypto.Cipher import PKCS1_OAEP


def asymmetric_decrypt():
    while 1:
        try:
            ct_path = input("Enter the CipherText file path")
            pt_path = input("Enter the PlainText file path and name")
            with open(ct_path, 'rb') as file:
                ct_text = file.read()
            private_key_loc = input("Enter location for the private key")
            key = RSA.importKey(open(private_key_loc).read())
            chunks = [ct_text[i:i + 256] for i in range(0, len(ct_text), 256)]
            cipher = PKCS1_OAEP.new(key)
            pt = b''
            for i in range(len(chunks)):
                pt += cipher.decrypt(chunks[i])
            with open(pt_path, 'wb') as file:
                file.write(pt)
            print("Correctly Decrypted content of file {0} to file {1}".format(ct_path, pt_path))
            repeat = input('Do you want to Decrypt another file ? [Y/N] ')
            if repeat.lower() == 'n':
                break
        except Exception as e:
            print(e)
            continue



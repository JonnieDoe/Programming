#!/usr/bin/python -tt

__author__ = "DC"
__version__ = "0.1"

import pickle
from base64 import b64encode
from base64 import b64decode
# need pycrypto package
# For Windows, when you install pycrypto you must rename the crypto folder into Crypto (case-sensitive)
# Python3.5\Lib\site-packages\crypto --> Python3.5\Lib\site-packages\Crypto
try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto import Random
except Exception as error:
    print("Error: ", error)
    exit()


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC="\033[3m"

def encrypt(key, msg):
    IV = Random.new().read(16)  # AES reads 16 byte blocks
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    # Remember the IV for decrypting
    try:
        with open("IV.txt", 'wb') as f:
            pickle.dump(IV, f)
            f.close()
    except (Exception, IOError) as error:
        print("Error writing IV to file: ", error)
        exit()

    if len(msg) %16 !=0:
        # We need to pad to fill the 16 byte block
        while (len(msg)%16 !=0):
            msg += "^"

    outputMsg = encryptor.encrypt(msg)
    print("Encrypted message: ", outputMsg)

    outputMsgB64 = b64encode(outputMsg)
    print("b64 encodes message: ", outputMsgB64)
    print("IV: ", IV)

def decrypt(key, msg, IV):
    encryptedMsg = b64decode(msg)
    #print(encryptedMsg)

    try:
        with open(IV, 'rb') as f:
            decryptIV = pickle.load(f)
            f.close()
    except (Exception, IOError) as error:
        print("Error on reading IV from file: ", error)
        exit()

    #print(decryptIV)
    decryptor = AES.new(key, AES.MODE_CBC, decryptIV)
    decryptedMsg = decryptor.decrypt(encryptedMsg)
    decryptedStrMsg = decryptedMsg.decode('utf-8').replace("^", "")
    print("Decoded message: " + "'" + colors.BOLD + decryptedStrMsg + colors.ENDC + "'")

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    #print(hasher.digest())
    return hasher.digest()

def main():
    choice = input("(E)ncrypt/(D)ecrypt?: ")

    if choice == 'E':
        msg = input("Message to encrypt: ")
        password = input("Key: ")
        encrypt(getKey(password), msg)
        print("Done.")
    elif choice == 'D':
        msg = input("Message to decrypt: ")
        password = input("Key: ")
        IV = input("IV location: ")
        decrypt(getKey(password), msg, IV)
        print("Done.")
    else:
        print("No option selected, closing...")

if __name__ == '__main__':
    main()
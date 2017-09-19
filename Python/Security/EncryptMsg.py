# !/usr/bin/python -tt
"""
    This script encrypts/decrypts the supplied message

    Requirements:
        pycrypto

        For Windows, when you install pycrypto you must rename the crypto folder into Crypto (case-sensitive)
        Python3.5\Lib\site-packages\crypto --> Python3.5\Lib\site-packages\Crypto

    Run the script:
        python EncryptMsg.py
"""


__author__ = "DC"
__version__ = "0.2"


import pickle
from base64 import b64encode
from base64 import b64decode

try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto import Random
except Exception as error:
    print("Error: ", error)
    exit()


class Colors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = "\033[3m"


#################################################################################################
# Encrypt function
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

    if len(msg) % 16 != 0:
        # We need to pad to fill the 16 byte block
        while len(msg) % 16 != 0:
            msg += "^"

    output_msg = encryptor.encrypt(msg)
    print("Encrypted message: ", output_msg)

    output_msg_b64 = b64encode(output_msg)
    print("b64 encodes message: ", output_msg_b64)
    print("IV: ", IV)


#################################################################################################
# Decrypt function
def decrypt(key, msg, IV):
    encrypted_msg = b64decode(msg)
    decrypt_IV = None
    #print(encrypted_msg)

    try:
        with open(IV, 'rb') as f:
            decrypt_IV = pickle.load(f)
            f.close()
    except (Exception, IOError) as err:
        print("Error on reading IV from file: ", err)
        exit()

    #print(decryptIV)
    decryptor = AES.new(key, AES.MODE_CBC, decrypt_IV)
    decrypted_msg = decryptor.decrypt(encrypted_msg)
    decrypted_str_msg = decrypted_msg.decode('utf-8').replace("^", "")
    print("Decoded message: " + "'" + Colors.BOLD + decrypted_str_msg + Colors.ENDC + "'")


#################################################################################################
# Key function
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))

    #print(hasher.digest())
    return hasher.digest()


#################################################################################################
# main() function
def main():
    choice = input("(E)ncrypt/(D)ecrypt?: ")

    if choice == 'E':
        msg = input("Message to encrypt: ")
        password = input("Key: ")
        encrypt(get_key(password), msg)
        print("Done.")
    elif choice == 'D':
        msg = input("Message to decrypt: ")
        password = input("Key: ")
        IV = input("IV location: ")
        decrypt(get_key(password), msg, IV)
        print("Done.")
    else:
        print("No option selected, closing...")


#################################################################################################
# Standard boilerplate to call the main() function to begin the program.
# This only runs if the module was *not* imported.
if __name__ == '__main__':
    main()

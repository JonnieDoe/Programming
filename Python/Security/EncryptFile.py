# !/usr/bin/python -tt
"""
    This script encrypts/decrypts the supplied file

    Requirements:
        pycrypto

        For Windows, when you install pycrypto you must rename the crypto folder into Crypto (case-sensitive)
        Python3.5\Lib\site-packages\crypto --> Python3.5\Lib\site-packages\Crypto

    Run the script:
        python EncryptFile.py
"""


__author__ = "DC"
__version__ = "0.2"


import os

try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto import Random
except Exception as error:
    print("Error: ", error)

    exit()


#################################################################################################
# Encrypt function
def encrypt(key, filename):
    chunk_size = 64 * 1024
    output_file = "(encrypted)" + filename
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)  # AES reads 16 byte blocks

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(file_size.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    # We need to pad to fill the 16 byte block
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


#################################################################################################
# Decrypt function
def decrypt(key, filename):
    chunk_size = 64 * 1024
    output_file = filename[11:]

    with open(filename, 'rb') as infile:
        file_size = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(file_size)


#################################################################################################
# Key function
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))

    return hasher.digest()


#################################################################################################
# main() function
def main():
    choice = input("(E)ncrypt/(D)ecrypt?: ")

    if choice == 'E':
        filename = input("File to encrypt: ")
        password = input("Pasword: ")
        encrypt(get_key(password), filename)

        print("Done.")
    elif choice == 'D':
        filename = input("File to decrypt: ")
        password = input("Pasword: ")
        decrypt(get_key(password), filename)

        print("Done.")
    else:
        print("No option selected, closing...")


#################################################################################################
# Standard boilerplate to call the main() function to begin the program.
# This only runs if the module was *not* imported.
if __name__ == '__main__':
    main()

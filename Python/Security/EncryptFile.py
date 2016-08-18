#!/usr/bin/python -tt

__author__ = "DC"
__version__ = "0.1"


import os
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


def encrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = "(encrypted)" + filename
    fileSize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)  # AES reads 16 byte blocks

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(fileSize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) %16 !=0:
                    # We need to pad to fill the 16 byte block
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[11:]

    with open(filename, 'rb') as infile:
        fileSize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(fileSize)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def main():
    choice = input("(E)ncrypt/(D)ecrypt?: ")

    if choice == 'E':
        filename = input("File to encrypt: ")
        password = input("Pasword: ")
        encrypt(getKey(password), filename)
        print("Done.")
    elif choice == 'D':
        filename = input("File to decrypt: ")
        password = input("Pasword: ")
        decrypt(getKey(password), filename)
        print("Done.")
    else:
        print("No option selected, closing...")

if __name__ == '__main__':
    main()




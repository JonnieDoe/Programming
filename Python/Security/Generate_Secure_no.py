#!/usr/bin/python -tt

__author__ = "DC"

import sys
import random
import time

# Banner
def banner():
    title = "Generate random numbers the proper way"
    version = "Version: 0.1"
    contact = "Author: DC"
    print("-" * 45)
    print(title.center(45))
    print(version.center(45))
    print(contact.center(45))
    print("-" * 45)


def generate_no():
    # Get local time
    localtime = time.asctime(time.localtime(time.time()))

    # Random bytes
    # bytes = os.urandom(32)
    rand = random.SystemRandom()

    # Random (probably large) integer
    integer = rand.randint(0, sys.maxsize)
    print("Your security number generated at [{time}] is: {sec_gen_no}".format(sec_gen_no=integer, time=localtime))


def main():
    """
    The main function
    """
    banner()
    generate_no()

if __name__ == '__main__':
    main()
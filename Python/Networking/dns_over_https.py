#!/usr/bin/python -tt

__author__ = "DC"
"""
    DNS over HTTPS
"""

import sys
import requests
import traceback

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

# Banner function
def banner():
    title = "DNS over HTTPS"
    version = "Version 1.0"
    contact = "David-Cristian"
    print("-" * 45)
    print(title.center(45))
    print(version.center(45))
    print(contact.center(45))
    print("-" * 45)

# Help menu
def print_help(text):
    print("Program takes 2 arguments: [DNS_query] and [DNS_type]\n\t EX: dns_over_https [google.com] [ANY]")

# Valid record types
def print_all(text):

    print("\n\t" + colors.BOLD + "DNS type options:" + colors.ENDC + colors.ITALIC + "[A] [AAAA] [CNAME] [MX] [ANY]" + colors.ENDC+"\n")

# Quit program function
def quit_prog(text):
    """Terminates the program."""
    print("Quitting the program...")
    sys.exit(1)


def check_input():
    """
        Function used to check the input transmitted to the program
    """
    # Input validation
    switch = {
        'help': print_help,
        'DNS_query_types': print_all,
        'go': execute,
        'quit': quit_prog
    }
    options = switch.keys()
    prompt = 'Pick an option from the list ({0}): '.format(', '.join(options))

    while True:
        opt = input(prompt)
        option = switch.get(opt, None)
        if option:
            option("")
        else:
            print("Please select a valid option!")

def execute(text):
    options = ['A', 'AAAA', 'CNAME', 'MX', 'ANY']
    prompt = 'Pick an option from the list ({0}): '.format(', '.join(options))
    while True:
        dns_type = input(prompt)
        if dns_type in options:
            while True:
                dns_query = input("DNS to query: ")
                if len(dns_query) < 2:
                    print("Please provide a valid DNS!")
                else:
                    print(str(dns_query))
                    https(dns_query, dns_type)
        else:
            print("Please select a valid DNS record type!")

# HTTPS function
def https(dns_query, query_type):
    link = "https://dns.google.com/resolve?name="+dns_query+"&type="+query_type+""
    try:
        reply = requests.get(link, timeout=2)
        #print(reply.text)
        #print(replay.json())
        answer = reply.text
        print(answer)

        sys.exit(1)
    except ConnectionError:
        print("Sorry! the request for [{0}] encountered a network problem".format(dns_query))
    except Exception:
        traceback.print_exc()

# Gather the code in a main() function
def main():
    """
    The main function
    """
    banner()
    check_input()

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

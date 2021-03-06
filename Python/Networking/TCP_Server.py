#!/usr/bin/python -tt

__author__ = "DC"


import socket
import threading
import ipaddress

# Banner function
def banner():
    title = "TCP Server"
    version = 'V: "1.0"'
    contact = 'Author: "DC"'
    print("-" * 45)
    print(title.center(45))
    print(version.center(45))
    print(contact.center(45))
    print("-" * 45)

def check_input():
    """
        Function used to check the input transmitted to the program
    """
    ip = "0.0.0.0"

    # Validate IP address
    while True:
        inp = input("Provide an IP address to listen on (or Enter for default: [0.0.0.0]): ")
        if not inp:
            break
        try:
            ip = str(ipaddress.ip_address(inp))
            #print(type(ip))
            #print(ip)
            break
        except (Exception, ValueError) as error:
            print("\tPlease enter a correct value as IP address to bind to\n\tError: {err}".format(err=error))

    # Validate Port Number
    while True:
        inp2 = input("Provide a port to bind to: ")
        try:
            port = int(inp2)
            #print(port)
            break
        except (Exception, ValueError) as error:
            print("\tPlease enter a correct value as port number\n\tError: {err}".format(err=error))
    tcp(ip, port)

# The server function
def tcp(ip, port):
    bind_ip = ip
    bind_port = port
    #print(bind_ip, bind_port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Listening on {ip}:{port}".format(ip=bind_ip, port=bind_port))

    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: {ip}:{port}".format(ip=addr[0], port=addr[1]))

        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

# This is our client-handling thread
def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)
    print("[*] Received: {req}".format(req=request))

    # send back a packet
    client_socket.send("ACK!")
    client_socket.close()

# Gather the code in a main() function
def main():
    """
    The main function
    """
    banner()
    check_input()
    """
        client, addr = server.accept()
        print("[*] Accepted connection from: {ip}:{port}".format(ip=addr[0], port=addr[1]))

        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
    """

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

import socket

__author__ = "DC"

"""
In this code snippet, we are making some serious assumptions about sockets that you definitely want to be aware of. The first assumption is that our connection will always succeed, and the second is that the server is always expecting us to send data first (as opposed to servers that expect to send data to you first and await your response). Our third assumption is that the server will always send us data back in a timely fashion. We make these assumptions largely for simplicity’s sake. While programmers have varied opinions about how to deal with blocking sockets, exception-handling in sockets, and the like, it’s quite rare for pentesters to build these niceties into the quick-and-dirty tools for recon or exploitation work, so we’ll omit them in this chapter.
"""

target_host = "www.google.com"
target_port = 80

# first create a socket object with the AF_INET and SOCK_STREAM parameters
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
# First specify the message and then encode it (it will not work as a simple string)
message = 'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'
client.send(message.encode('utf-8'))

# receive some data
response = client.recv(4096)
print(response)

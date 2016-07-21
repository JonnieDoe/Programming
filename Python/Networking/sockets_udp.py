import socket

__author__ = "DC"

"""
In this code snippet, we are making some serious assumptions about sockets that you definitely want to be aware of. The first assumption is that our connection will always succeed, and the second is that the server is always expecting us to send data first (as opposed to servers that expect to send data to you first and await your response). Our third assumption is that the server will always send us data back in a timely fashion. We make these assumptions largely for simplicity’s sake. While programmers have varied opinions about how to deal with blocking sockets, exception-handling in sockets, and the like, it’s quite rare for pentesters to build these niceties into the quick-and-dirty tools for recon or exploitation work, so we’ll omit them in this chapter.
"""

target_host = "104.155.16.99"
target_port = 1194

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
message = "AAABBBCCC"
client.sendto(message.encode('utf-8'),(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)
print(data)

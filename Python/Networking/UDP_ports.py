## Check UDP Ports
import socket
import dns.resolver

IP = "8.8.8.8"
PORT = 53
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MESSAGE = "Hello"

#sock.sendto(MESSAGE, (IP, PORT))
sock.sendto(bytes(MESSAGE, 'utf-8'), (IP, PORT))
print(sock.recv(10240))

## Output
print("UDP target IP:", IP)
print("UDP target port:", PORT)
print("Message:", MESSAGE)
print("Received message:", RECV)

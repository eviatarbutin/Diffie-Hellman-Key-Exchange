import socket
import random


IP = "127.0.0.1"
PORT = 1337
BUFFER = 4096

print("Client is up:")
client_socket = socket.socket()
client_socket.connect((IP,PORT))
print("client connected")

N = int(client_socket.recv(BUFFER))
G = int(client_socket.recv(BUFFER))
A = int(client_socket.recv(BUFFER))

b = random.randint(N//4,N//2)
B = G**b%N
client_socket.send(bytes(B))

print(f"N: {N}\nG: {G}\nb:{b}\nB:{B}")

key = A**b%N
print(f"A:{A}\nkey:{key}")

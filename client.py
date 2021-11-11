import socket
import random


IP = "127.0.0.1"
PORT = 1337
BUFFER = 4096

print("Client is up:")
client_socket = socket.socket()
client_socket.connect((IP,PORT))
print("client connected")

N = int(client_socket.recv(BUFFER).decode())
print(f"N: {N}")

G = int(client_socket.recv(BUFFER).decode())
print(f"G: {G}")

A = int(client_socket.recv(BUFFER).decode())
print(f"A: {A}")

b = random.randint(N//4,N//2)
B = G**b%N
client_socket.send(str(B).encode())

print(f"b:{b}\nB:{B}")

key = A**b%N
print(f"A:{A}\nkey:{key}")

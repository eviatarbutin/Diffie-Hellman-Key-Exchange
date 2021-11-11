import socket
import random


IP = "0.0.0.0"
PORT = 1337
BUFFER = 4096
NUMBER_OF_CLIENTS = 1
N_NUMBER_OF_BITS = 2**100
print("Server is up:")
server_socket = socket.socket()
server_socket.bind((IP,PORT))
server_socket.listen(NUMBER_OF_CLIENTS)
client_socket, client_address = server_socket.accept()
print(f"{client_address} connected")

N = random.randint(N_NUMBER_OF_BITS//2,N_NUMBER_OF_BITS)
print(f"N: {N}")
G = 37
print(f"G: {G}")
a = random.randint(N//8,N//4)
print(f"a: {a}")
A = G**a%N
print(f"A: {A}")
client_socket.send(bytes(N))
client_socket.send(bytes(G))
client_socket.send(bytes(A))

B = int(client_socket.recv(BUFFER))
key = B**a%N
print(f"B:{B}\nkey:{key}")

client_socket.close()
server_socket.close()


import socket
import random


IP = "0.0.0.0"
PORT = 1337
BUFFER = 4096
NUMBER_OF_CLIENTS = 1
N_range = 4000
print("Server is up:")
server_socket = socket.socket()
server_socket.bind((IP,PORT))
server_socket.listen(NUMBER_OF_CLIENTS)
client_socket, client_address = server_socket.accept()
print(f"{client_address} connected")

N = random.randint(N_range//2,N_range)
client_socket.send((str(N)+"\n").encode())
print(f"N: {N}")

G = 37
print(f"G: {G}")
client_socket.send((str(G)+"\n").encode())

a = random.randint(N//8,N//4)
print(f"a: {a}")
A = G**a%N
print(f"A: {A}")
client_socket.send((str(A)+"\n").encode())

B = int(client_socket.recv(BUFFER).decode())
key = B**a%N
print(f"B:{B}\nkey:{key}")

client_socket.close()
server_socket.close()


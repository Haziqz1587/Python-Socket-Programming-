import socket

HOST = '192.168.153.129'  # The server's hostname or IP address
PORT = 8080         # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        radius = input("Enter the radius of the sphere (or 'quit' to exit): ")
        if radius.lower() == 'quit':
            break
        s.sendall(radius.encode())
        data = s.recv(1024).decode()
        print("Sphere volume:", data)

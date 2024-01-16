import socket

HOST = '192.168.153.129'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            try:
                radius = float(data)
                volume = (4/3) * 3.14159 * radius**3
                conn.sendall(str(int(volume)).encode())
            except ValueError:
                conn.sendall(b"Invalid radius value")

import socket

def server_program():
    host = "172.16.31.240"
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from:", address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("Received from client:", data)

        try:
            # split the incoming string into 2 numbers
            num1, num2 = data.split()
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2       # perform addition

            conn.send(str(result).encode())

        except:
            conn.send("Invalid input! Send two numbers.".encode())

    conn.close()

if __name__ == "__main__":
    server_program()

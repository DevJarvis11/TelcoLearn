import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        num1 = input("Enter first number (or 'bye' to exit): ")
        if num1.lower() == "bye":
            break

        num2 = input("Enter second number: ")

        # send both numbers as a single string: "num1 num2"
        message = f"{num1} {num2}"
        client_socket.send(message.encode())

        result = client_socket.recv(1024).decode()
        print("Result from server:", result)

    client_socket.close()

if __name__ == "__main__":
    client_program()

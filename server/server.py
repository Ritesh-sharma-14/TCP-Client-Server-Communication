import socket
import datetime

IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(ADDRESS)

print("SERVER IS STARTING...")

serverSocket.listen(3)

while True:
    connection, address = serverSocket.accept()

    print("Connection from:", address)

    # Send welcome message
    connection.send(
        f"Hello from server! You are connected to {IP_SERVER}:{PORT}".encode("utf-8")
    )

    # Receive question from client
    question = connection.recv(1024).decode("utf-8")

    print("Question received from client:", question)

    # Prepare response
    if question == "1":
        response = "Current time is: " + datetime.datetime.now().strftime("%H:%M:%S")

    elif question == "2":
        response = "Today's date is: " + datetime.datetime.now().strftime("%Y-%m-%d")

    else:
        response = "Invalid option. Choose 1 or 2."

    # Send response
    connection.send(response.encode("utf-8"))

    connection.close()
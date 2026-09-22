import socket

IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect(ADDRESS)

    print("Client is connected to server at:", ADDRESS)

    # Receive welcome message
    message = clientSocket.recv(1024).decode("utf-8")

    print("Message from server:", message)

    while True:
        try:
            question = int(input("Choose a question (1/2): "))

            if question == 1 or question == 2:
                clientSocket.send(str(question).encode("utf-8"))
                break
            else:
                print("Please enter only 1 or 2")

        except ValueError:
            print("Enter a number only")

    # Receive server answer
    answer = clientSocket.recv(1024).decode("utf-8")

    print("Server answer:", answer)

except ConnectionRefusedError:
    print("Server is not running or wrong IP/PORT")

finally:
    clientSocket.close()
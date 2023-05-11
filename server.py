import socket

def run_server():
    # define host and port
    host = '127.0.0.1'  # change this to your desired IP address
    port = 5000  # change this to your desired port number

    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket object to a specific address and port
    server_socket.bind((host, port))

    # listen for incoming connections
    server_socket.listen(1)

    print('Waiting for client...\n')

    # accept incoming connections
    conn, addr = server_socket.accept()

    # receive the message from the client
    data = conn.recv(1024)
    message = data.decode('utf-8')
    print(f"Received message from client: {message}\n")

    # send a response to the client
    response = "Hello, How can I assist you?"  # change this to your desired response message
    conn.send(response.encode('utf-8'))

    # receive the name from the client
    data = conn.recv(1024)
    name = data.decode('utf-8')
    print(f"Received name from client: {name}\n")

    # send a welcome message to the client
    welcome_message = f"Hello {name}, Welcome to my server!"  # change this to your desired welcome message
    conn.send(welcome_message.encode('utf-8'))

    # close the connection
    conn.close()

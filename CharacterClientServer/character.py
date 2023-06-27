import socket

def count_characters(input_str):
    count = 0
    for char in input_str:
        if char != ' ':
            count += 1
    return count

def handle_client(client_socket):
    input_str = client_socket.recv(1024).decode('utf-8')
    count = count_characters(input_str)
    client_socket.send(str(count).encode('utf-8'))
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print('Server is running and listening for incoming connections...')
    while True:
        client_socket, client_address = server_socket.accept()
        print('Received incoming connection from:', client_address)
        handle_client(client_socket)

start_server()
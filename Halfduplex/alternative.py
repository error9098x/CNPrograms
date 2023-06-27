import socket

def count_characters(input_str):
    count = 0
    for char in input_str:
        if char != ' ':
            count += 1
    return count

def handle_client(client_socket):
    while True:
        # receive input string from client
        input_str = client_socket.recv(1024).decode('utf-8')
        if not input_str:
            break
        print('Received input string from client:', input_str)
        
        # count characters in input string
        count = count_characters(input_str)
        print('Counted', count, 'characters in input string')
        
        # send character count to client
        client_socket.send(str(count).encode('utf-8'))
        print('Sent character count', count, 'to client')
    
    client_socket.close()
    print('Closed connection to client')

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print('Server is running and listening for incoming connections...')
    while True:
        client_socket, client_address = server_socket.accept()
        print('Received incoming connection from:', client_address)
        handle_client(client_socket)

def send_input_string(input_str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    client_socket.send(input_str.encode('utf-8'))
    count = client_socket.recv(1024).decode('utf-8')
    client_socket.close()
    return int(count)

def start_client():
    while True:
        # prompt user for input string
        input_str = input('Enter an input string (or "quit" to exit): ')
        if input_str == 'quit':
            break
        
        # send input string to server and receive character count
        count = send_input_string(input_str)
        
        # print character count to console
        print('The character count of the input string is:', count)

    print('Exiting client')

# start the server in a separate thread
import threading
server_thread = threading.Thread(target=start_server)
server_thread.start()

# start the client in the main thread
start_client()

# wait for the server thread to finish
server_thread.join()

print('Exiting program')
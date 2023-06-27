import socket

def byte_stuffing(input_str):
    flag = "flag"
    esc = "esc"
    stuffed_str = flag

    for i in range(len(input_str)):
        if input_str[i] == flag or input_str[i] == esc:
            stuffed_str += esc
        stuffed_str += input_str[i]

    stuffed_str += flag
    return stuffed_str

def handle_client(client_socket):
    while True:
        # receive input string from client
        input_str = client_socket.recv(1024).decode('utf-8')
        if not input_str:
            break
        print('Received input string from client:', input_str)
        
        # stuff input string
        stuffed_str = byte_stuffing(input_str)
        print('Stuffed input string:', stuffed_str)
        
        # send stuffed string to client
        client_socket.send(stuffed_str.encode('utf-8'))
        print('Sent stuffed string to client:', stuffed_str)
    
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

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    
    while True:
        # prompt user for input string
        input_str = input('Enter an input string (or "quit" to exit): ')
        if input_str == 'quit':
            break
        
        # send input string to server and receive stuffed string
        client_socket.send(input_str.encode('utf-8'))
        stuffed_str = client_socket.recv(1024).decode('utf-8')
        print('Received stuffed string from server:', stuffed_str)
        
        # unstuff stuffed string
        output_str = ""
        flag = "flag"
        esc = "esc"
        i = 0
        while i < len(stuffed_str):
            if stuffed_str[i:i+len(flag)] == flag:
                i += len(flag)
            elif stuffed_str[i:i+len(esc)] == esc:
                output_str += stuffed_str[i+len(esc)]
                i += len(esc) + 1
            else:
                output_str += stuffed_str[i]
                i += 1
        
        print('Unstuffed output string:', output_str)

    client_socket.close()
    print('Exiting client')

# start the server in a separate thread
import threading
threading.Thread(target=start_server).start()

# start the client
start_client()
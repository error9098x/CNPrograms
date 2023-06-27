import socket

def send_input_string(input_str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))
    client_socket.send(input_str.encode('utf-8'))
    count = client_socket.recv(1024).decode('utf-8')
    client_socket.close()
    return int(count)

input_str = input('Enter a string to count its characters: ')
count = send_input_string(input_str)
print('The character count of the input string is:', count)
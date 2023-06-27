import socket

def crc32(data):
    crc = 0xFFFFFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ (0xEDB88320 * (crc & 1))
    return crc

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("Enter message to send: ")
    s.sendall(message.encode())
    data = s.recv(1024)
    checksum = crc32(message.encode())
    if int(data) == checksum:
        print('Checksums match!')
    else:
        print('Checksums do not match.')
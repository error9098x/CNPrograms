class IP_Address:
    def __init__(self, address):
        self.address = address
        self.network = None
        self.host = None
        self.classful_addressing()
    
    def classful_addressing(self):
        first_byte = self.address.split('.')[0]
        first_byte = int(first_byte)
        if first_byte >= 0 and first_byte <= 127:
            self.network = self.address.split('.')[0]
            self.host = '.'.join(self.address.split('.')[1:])
            self.classful = 'Class A'
        elif first_byte >= 128 and first_byte <= 191:
            self.network = '.'.join(self.address.split('.')[0:2])
            self.host = '.'.join(self.address.split('.')[2:])
            self.classful = 'Class B'
        elif first_byte >= 192 and first_byte <= 223:
            self.network = '.'.join(self.address.split('.')[0:3])
            self.host = self.address.split('.')[3]
            self.classful = 'Class C'
        elif first_byte >= 224 and first_byte <= 239:
            self.classful = 'Class D'
        else:
            self.classful = 'Class E'
    
    def __str__(self):
        return f'IP Address: {self.address}\nClassful Addressing: {self.classful}\nNetwork: {self.network}\nHost: {self.host}'

ip = IP_Address('192.168.1.1')
print(ip)
ip = IP_Address('10.10.200.6')
print(ip)
ip = IP_Address('172.15.165.1')
print(ip)
ip = IP_Address('230.10.65.30')
print(ip)
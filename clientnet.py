import socket


class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connection (self):
        self.client.connect(("localhost", 2001))

    def SendPhoto(self,imgpath):
        data = 'A'
        self.client.send(data.encode('utf-8'))

        file = open(imgpath, mode="rb")
        data = file.read(2048)
        while data:
            self.client.send(data)
            data = file.read(2048)

        file.close()

    def SendFIO(self,FIO):
        data = 'F'
        self.client.send(data.encode('utf-8'))

        data = FIO
        self.client.send(data.encode('utf-8'))

    def SendMethod(self,method):
        data = 'M'
        self.client.send(data.encode('utf-8'))

        data = method
        print(data)
        self.client.send(data.encode('utf-8'))

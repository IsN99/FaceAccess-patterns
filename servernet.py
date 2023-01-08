import socket

class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 3110))
        self.server.listen(10)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.dataId = None
        self.data = None

        self.client_socket = None
        self.client_address = None

        self.path = 'tempimage.png'
        self.FIO = None
        self.id = None

        self.block = False

        self.logic()

    def logic(self):
        self.client_socket, self.client_address = self.server.accept()
        while True:
            self.dataId = self.client_socket.recv(1).decode('utf-8')
            if self.dataId == 'A':
               self.RecvPhoto()

            elif self.dataId == 'F':
               self.RecvFIO()

            elif self.dataId == 'M':
               self.RecvMethod()

            elif self.dataId == 'I':
               self.RecvId()

    def RecvPhoto (self):
        import math
        size = self.RecvPhotoSize()
        size = math.ceil(size/1024)
        file = open(self.path, mode="wb")
        while size>0:
            self.data = self.client_socket.recv(1024)
            file.write(self.data)
            size-=1
        file.close()
        self.Next()

    def RecvId (self):
        self.id = self.client_socket.recv(1024).decode('utf-8')
        self.Next()

    def RecvPhotoSize (self):
        self.data = self.client_socket.recv(1024).decode('utf-8')
        return int(self.data)

    def RecvFIO  (self):
        self.FIO = self.client_socket.recv(1024).decode('utf-8')
        self.Next()

    def RecvMethod  (self):
        self.method = self.client_socket.recv(1024).decode('utf-8')


    def Next (self):
        if not self.block:
            self.client.connect(("localhost", 3100))
            self.block = True
        self.client.send('nxt'.encode('utf-8'))

Server()
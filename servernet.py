import socket

class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 2001))
        self.server.listen()

        self.data = None

        self.client_socket = None
        self.client_address = None

        self.path = 'tempimage.png'
        self.FIO = None
        self.id = None

        self.logic()

    def logic(self):
        while True:
            self.client_socket, self.client_address = self.server.accept()
            self.data = self.client_socket.recv(1).decode('utf-8')
            if self.data == 'A':
               self.RecvPhoto()

            elif self.data == 'F':
               self.RecvFIO()


            elif self.data == 'M':
               print('debug')
               self.RecvMethod()


    def RecvPhoto (self):
        file = open(self.path, mode="wb")
        self.data = self.client_socket.recv(1024)
        while self.data:
            file.write(self.data)
            self.data = self.client_socket.recv(1024)

        file.close()

    def RecvFIO  (self):
        self.FIO = self.client_socket.recv(1024).decode('utf-8')
        print(self.FIO)

    def RecvMethod  (self):
        print("debug")
        self.method = self.client_socket.recv(1024).decode('utf-8')



Server()
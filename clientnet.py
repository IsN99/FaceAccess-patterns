import socket


class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.block = False


    def Connection (self):
        self.client.connect(("localhost", 3110))

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 3100))


    # def Disconnect (self):
    #     self.client.shutdown(socket.SHUT_RDWR)
    #     self.client.close()

    def SendPhoto(self,imgpath):
        data = 'A'
        self.client.send(data.encode('utf-8'))
        self.SendPhotoSize(imgpath)

        file = open(imgpath, mode="rb")
        while True:
            data = file.read(1024)
            if not data:
                break
            self.client.send(data)
        file.close()

    def SendPhotoSize(self,imgpath):
        from os import stat
        data = str(stat(imgpath).st_size)
        self.client.send(data.encode('utf-8'))

    def SendFIO(self,FIO):
        data = 'F'
        self.client.send(data.encode('utf-8'))
        data = FIO
        self.client.send(data.encode('utf-8'))

    def SendId (self,Id):
        data = 'I'
        self.client.send(data.encode('utf-8'))
        data = Id
        self.client.send(data.encode('utf-8'))

    def SendMethod(self,method):
        data = 'M'
        self.client.send(data.encode('utf-8'))
        data = method
        self.client.send(data.encode('utf-8'))

    def WaitForNext (self):
        if not self.block:
            self.server.listen()
            self.client_socket, self.client_address = self.server.accept()
            self.block = True
        temp = self.client_socket.recv(3).decode('utf-8')


import socket
import pickle


class Network:
    def __init__(self,serverip):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverip = serverip
        self.port = 5555
        self.addr = (self.serverip,self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            print("server not found!")
    
    def getInit(self):
        return self.p

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


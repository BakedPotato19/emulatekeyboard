import sys
import pickle
from _thread import *
import socket
import typing
from ..Keyboard.KeyboardEmulator import emulator

class Server():
    def __init__(self,Ip_address : str, Port : str):
        self.Port = Port
        self.Ip_address = Ip_address
        self.Connections = {}

        self.emu = emulator()

        self.Running = True 

        self.Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Server.setsockopt(socket.SOL_IP,socket.SO_REUSEADDR,1)

    def StartServer(self):
        try:
            self.Server.bind((self.Ip_address,self.Port))
        except socket.error as e:
            str(e)
        
        self.Server.listen(1)
        print('Waiting for connection. Server started at ip:',self.Ip_address)

    def ServerLoop(self):
        CurrentPlayerId = 0

        while self.Running:
            print("serverloop running")
            conn, addr = self.Server.accept()
            print("Connected to", addr)
            ###
            start_new_thread(self.__ThreadedClient,(conn,CurrentPlayerId))
            CurrentPlayerId += 1

    def __ThreadedClient(self, connection, playerid : int): 
        ### dummy for test
        connection.send(pickle.dumps("start"))

        while True:
            data = self.RecieveFromClient(connection)
            if not data == "dummy":

                self.emu.write(str(data))

            if not data:
                break
            else:
                self.SendToClient(connection,"succesful")
                pass

        ## On disconnection
        print("Disconnected : ",connection)

    def SendToClient(self, connection : socket, data):
        try:
            connection.sendall(pickle.dumps(data))
            return True
        except:
            return False

    def RecieveFromClient(self, connection : socket):
        try:
            return pickle.loads(connection.recv(2048))
        except Exception as e:
            return False
         
    def RecieveFromClientById(self, playerid : id):
        return self.RecieveFromClient(self.Connections[playerid])


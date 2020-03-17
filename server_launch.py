from src.server.Server.Server import Server
from src.server.Server.Ip_address import Ip_address

if __name__ == "__main__":
    ip = Ip_address()
    
    server = Server(ip.GetIp(),5555)
    server.StartServer()
    server.ServerLoop()

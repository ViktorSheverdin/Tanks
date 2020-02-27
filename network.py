import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.65.0.202"
        self.port = 5555
        self. addr = (self.server, self.port)
        self.playerInfo = self.connect()

    def getPlayerInfo(self):
        return self.playerInfo

    def getAllPlayers(self):
        all_players_list = pickle.loads(self.client.recv(2048))

        return all_players_list

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

# n = Network()
# print("PlayerID is: ", n.getPlayerID())
# n.send("Network module is connected")
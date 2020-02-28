import socket
import sys
import pickle
from _thread import *
from network import Network
from player import Player
from random import randint

server = "10.65.0.202"
port = 5555
gameID = 0
playerID = 0
games = {}
players_on_server = []

# Creates a socket and init the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the port to the local server
try:
    s.bind((server, port))
except socket.error as e:
    print(e)
 
# Always listens for the other connections
s.listen()
print("Waiting for connection, Server Started")

def threaded_client(conn, playerID, gameID):
    new_player = Player(playerID, 150, 150, (255,0,200), 100, 100)

    print("Sending PlayerID")
    players_on_server.append(new_player)
    conn.send(pickle.dumps(new_player))
    print("PlayerID was sent")
    
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            print("Received data when connected :\n", data)
            if (data.playerID == playerID):
                players_on_server[playerID] = data
            print("players_on_server",players_on_server[playerID])
            if not data:
                print("Disconnected from the server")
                players_on_server.pop(int(data.playerID))
                break
            else:
                print("All players on the server: \n", players_on_server)
            
                conn.sendall(pickle.dumps(players_on_server))
            #conn.send(pickle.dumps(players_on_server))
        except:
            break

    print("Connection lost")
    conn.close()

while True:
    # Always accept the connection
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # After the connection was accepted, start multythreading so many connections could be established simoltaniously
    start_new_thread(threaded_client, (conn, playerID, gameID))
    playerID += 1
    #conn.send(pickle.dumps(players_on_server))
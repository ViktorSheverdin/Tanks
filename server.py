import socket
import sys
import pickle
from _thread import *
from network import Network
from player import Player

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
    new_player = Player(playerID, 50, 50, (255,0,200), 100, 100)

    print("Sending PlayerID")
    players_on_server.append(new_player)
    conn.send(pickle.dumps(new_player))
    playerID += 1
    print("PlayerID was sent")
    
    reply = ""
    while True:
        try:
            conn.send(pickle.dumps(players_on_server))
            data = pickle.loads(conn.recv(2048))
            #print("Received data when connected :\n", data)
            players_on_server[playerID] = data
            if not data:
                print("Disconnected from the server")
                break
            else:
                reply = "Confirmation of connected"
                print("Received: ", data)
                print("Current player ID is: ", playerID)
            
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
    #conn.send(pickle.dumps(players_on_server))
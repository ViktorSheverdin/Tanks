import socket
import sys
import pickle
from _thread import *

server = "10.65.0.202"
port = 5555
gameID = 0
playerID = 0

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
    #conn.send(str.encode(str(playerID)))
    print("Sending PlayerID")
    #conn.send(str.encode(str(playerID)))
    conn.send(pickle.dumps(playerID))
    print("PlayerID was sent")

while True:
    # Always accept the connection
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # After the connection was accepted, start multythreading so many connections could be established simoltaniously
    start_new_thread(threaded_client, (conn, playerID, gameID))
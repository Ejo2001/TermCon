#Import the neccesary libraries
import getpass
import socket
import sys
import time
import codecs

#Gather the neccessary components for the connection
Hostname = input("Hostname: ") 
Port = input("Port: ")
ADDR = (Hostname, int(Port))
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect. If successfull, print and save the name of the node, and print the system specs provided. If not successfull, turn off the program
try:
    Client.connect(ADDR)
    Node = Client.recv(2048).decode('utf-8')
    print("Connected to", Node)
    print(Client.recv(2048).decode('utf-8'))
except:
    sys.exit()


#The message system. If you write "end" then quit.
def Send(msg):
    Message = msg.encode('utf-8')
    Client.send(Message)
    if msg == "end":
        Client.close()
        sys.exit()
    print(Client.recv(2048).decode('utf-8'))


#Repeat input while connected
while True:
    Send(input(Node + ": $ "))




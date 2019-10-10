import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port=1234
address=(ip,port)
server.bind(address)
server.listen(6)
print("started listening %s : %s" % (ip,port))
client,addr=server.accept()
print("got a connection %s : %s" % (addr[0],addr[1]))
while True:
    data=client.recv(1024).decode("utf-8")
    print("recieved %s from the client" % (data))
    print("processing data")
    if data=="Hello server" :
        mystring="Hello client"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        print("processing done \n reply sent")
    elif data=="This is your client" :
        mystring="Hello client"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        print("processing done \n reply sent")
    elif data=="VIRUS" :
        mystring="Infected Client sending VIRUS"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        client.close()
    elif data=="I just want to say LOVE YOU SAN!!" :
        mystring="Infected Client sending MALWARE"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        client.close()
       # print("processing done \n reply sent")\
    elif data=="fix your" :
        mystring="Infected Client sending Netsky sasser"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        client.close()
    elif data=="Stop making money" :
        mystring="Infected Client sending blaster worm"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        client.close()
    elif data=="how are you" :
        mystring="Please send your files for scanning"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        print("processing done \n reply sent")
    elif data=="DOM" :
        mystring="Infected Client sending TROJAN"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        print("processing done \n reply sent") 
        client.close()       
    elif data=="disconnect" :
        mystring="GoodBye"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        client.close()
        break
    else:
        mystring="Invalid data"
        b = bytes(mystring, 'utf-8')
        client.send(b)
        print("processing done \n Invalid data reply sent")

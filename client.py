import socket
client=socket.socket()
client.connect(('192.168.64.31',1234))
mystring="hgjhgjh"
b = bytes(mystring, 'utf-8')
client.send(b)
client.recv(1024)
def communicate(data):
    mystring=data
    b = bytes(mystring, 'utf-8')
    client.send(b)
    print(client.recv(1024).decode("utf-8"))
    return 


#Binary/              hexadecimal code
#Decimal			                                          keywords                      viruses
#0  		00  00-6D  73   62  6C       	 msbl                                                   phising
#0 	 	6A  75-73   74  20  77   		 I just want to say LOVE YOU SAN!!                       malware
#9	  	20  4C-4F  56  45  20  		                                              storm worm
#0 	 62  69-6C  6C  79  20  		 software!!                                           Concept virus
#0	  64  6F-20  79  6F  75     		D  are  low    cjfnol        sdnamw                  Melissa virus
#3  	20  70-6F  73  73  69     		Stop making money                                  blaster worm
#0 	 20  6D-61  6B  69  6E    		fix your                                            netsky sasser

#E 	 64  20-66  69  78  20
#7 	  61  72-65  21  21  00		DOM                                                        trojan
#0  	00  00-7F  00  00  00
#0 	 00  00-01  00  01  00
#0 	 00  00-00  00  00  46
#C	  C9 11-9F  E8  08  00
#0 	 00  03-10  00  00  00
#3  	00  00-01  00  04   00 

communicate("is this really working!!!")
communicate("Hello server")
communicate("This is your client")
communicate("how are you")
communicate("this is my downloaded file from https://google.com")
communicate("I just want to say LOVE YOU SAN!!")
communicate("Stop making money ")    
communicate("DOM") 
communicate("fix your")
communicate("disconnect")

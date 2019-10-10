# Infected-node-finder

The always connected world of internet is a soft target for viruses. Hence, we need a mechanism that protects files and other documents in the computer from very harmful viruses which can cause huge damage.
The goal is basically to check whether any client(s) i.e one or more nodes connected to the network are infected due to accessing any malicious website, and if yes, to identify which particular node/nodes are infected by displaying the respective ip addresses.
Signature scanning is a method of detecting a virus by scanning a target program to detect the presence of any virus signature. Virus signature is a unique string of bits, or the binary pattern, of a virus. The virus signature is like a fingerprint in that it can be used to detect and identify specific viruses. Anti-virus software uses the virus signature to scan for the presence of malicious code. If the signature is found in the target program, then it is considered as infected otherwise the target program is considered as uninfected.

In this project I have first created a client -server based system using python.
The different PC’s connected to this server act as nodes forming a small network. The clients hit on the server and the server identifies the respective port numbers of the client.
These nodes can access different sources of information on the internet. Nodes/clients get infected when they download certain particular files from the internet.
In the sever database a list of viruses and their respective hexadecimal code signatures is uploaded. If any client accesses any file and downloads it, then the server checks the file downloaded and compares it with the available codes in the database. If any code finds a match, then this means that the file contains malicious information and that particular client is infected. The server then informs the client that it is infected with which particular malware.

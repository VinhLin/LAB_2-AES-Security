import socket
import sys
from Cryptodome.Cipher import AES

SERVER_IP = "127.0.0.1"    #server IP of 127.0.0.1
# SERVER_IP = "192.168.1.101" #Server IP 
SERVER_PORT = 9000   #Server Port
CIPHER_KEY=b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r' #Shared Key 32 bytes for 256-bit encryption
TCP_BUFFER= 1024 #Buffer for receiving data
NONCE=b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t' #shared nonce key for validation. 
          
TCPserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize TCP stream
TCPserver.bind((SERVER_IP, SERVER_PORT)) #Bind TCP Stream connection
TCPserver.listen(1) #Listen for two TCP connections



conn, addr = TCPserver.accept() #connecting with client
print('Client A Connected From:', addr)
print()

while True:
	print("Receiving Secret Encrypted Message...")
	print()
	data=conn.recv(TCP_BUFFER) #Client cipher message
	ciphertext=data
	print("Received Encrypted Message:",ciphertext)
	print()
	cipher = AES.new(CIPHER_KEY, AES.MODE_EAX,NONCE) #AES encryption using EAX mode for Encryption and authentication 
	plaintext = cipher.decrypt(ciphertext) #decryption of the cipher message that we received from the client
	print("Decrypting using Shared Key...")
	print(plaintext)
	print("data:", data)
	break

print("Goodbye!")
TCPserver.close()














































#Credit To:
#TCP server coded by Anthony Wilkinson

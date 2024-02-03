import socket
import sys
import re
import getpass
from Cryptodome.Cipher import AES

SERVER_IP = "127.0.0.1"    #server IP of 127.0.0.1
SERVER_PORT = 9000         # server Port
CIPHER_KEY=b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r' #Shared Encryption/decryption Key
NONCE=b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t' #shared NONCE key for validity

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket creation
client.connect((SERVER_IP, SERVER_PORT)) #TCP connection


while True:
	Secret_Message_Input= getpass.getpass(prompt='Please Enter the Secret Message: ')
	print("Message will Encrypt with AES-256")
	print()
	raw_message=Secret_Message_Input.encode() #Encode message to bytes
	CIPHER = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE) #AES encryption using EAX mode with predefined cipher key and nonce key for validation
	ciphertext, tag = CIPHER.encrypt_and_digest(raw_message)
	print("Sending Encrypted Message:",ciphertext)
	client.send(ciphertext) #send ciphertext of raw message
	client.close()#closing the socket
	print()
	break

client.close()
print('Message Sent..Goodbye')
print()

# LAB_2-AES-Security
- This lab uses a secure method such as Advanced Encryption Standard (AES) which is widely used as a cryptographic algorithm that uses keys to encrypt/decrypt data. 
- Therefore, we will run server/client scripts to encrypt data, to simplify we will use localhost.
- what we need:
	- A PC runs Python code.
	- Install Wireshark, purpose capture traffic.
- First, create folder `LAB_2-AES-Security`:
```
mkdir LAB_2-AES-Security
cd LAB_2-AES-Security
```

### Step 1: [MIMT Attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) read Raw-data.
- Here, we use [Python Socket Programming - Server, Client Example](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- Open [Wireshark](https://www.wireshark.org/download.html), choose **Adapter for loopback traffic capture**.
- Also open 2 terminal and run code: 
	- Terminal 1: `python3 socket_client.py`
	- Terminal 2: `python3 socket_server.py`
- Community between server and client, we use can see data when use wireshark.
- ![Image 1](https://github.com/VinhLin/LAB_2-AES-Security/blob/main/MIMT_Attack/Image_1.png)
- ![Image 2](https://github.com/VinhLin/LAB_2-AES-Security/blob/main/MIMT_Attack/Image_2.png)

### Step 2: Encryption data use AES
- Install library [pycryptodome](https://github.com/Legrandin/pycryptodome):
```
pip install pycryptodome
pip install pycryptodomex
```
- Create folder:
```
mkdir Lab-2-AES/AES-First-Demo
cd Lab-2-AES/AES-First-Demo
```
- Like step 1, open Wireshark and two terminal. Run code:
```
python3 Server.py
python3 Client.py
```
- The result is Wireshark cannot read data.
- ![Result](https://github.com/VinhLin/LAB_2-AES-Security/blob/main/AES-First-Demo/Result.png)

---------------------------------------------------------------------------------------
## [RSA-Encryption](https://opensource.com/article/21/4/encryption-decryption-openssl)
```
mkdir RSA-Encryption
cd RSA-Encryption
```
- RSA Key exchange is widely used for the exchange of cryptographic keys over a public channel.
- We use [OpenSSL Library](https://www.openssl.org/), check version:
```
openssl version
```
- Create a **private-key** (`Pass phrase I use basic is: 123456`): 
```
openssl genrsa -aes128 -out vinhlin-private.pem 1024
openssl rsa -in vinhlin-private.pem -pubout > vinhlin-public.pem
```
- Copy file **vinhlin-private.pem** to client:
```
mkdir client
mv vinhlin-private.pem client/
```
- Create a text file: 
```
nano secret.txt
```
- Content: `Hello, I am WSL`.
- Encryption data of file **secret.txt**:
```
openssl rsautl -encrypt -inkey vinhlin-public.pem -pubin -in secret.txt -out secret.enc
```
- After, we send file **secret.enc** to client:
```
mv secret.enc client/
cd client/
```
- If client want read content, need use key `vinhlin-private.pem`.
```
openssl rsautl -decrypt -inkey vinhlin-private.pem -in secret.enc > decryptsecret_secret.txt
cat decryptsecret_secret.txt
```
- Result will is: `Hello, I am WSL`.
















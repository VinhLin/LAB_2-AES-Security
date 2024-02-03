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











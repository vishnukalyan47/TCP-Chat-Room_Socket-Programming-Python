import threading
import socket			

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	


nickname = input('Choose a nickname : ')

client.connect(('127.0.0.1', 5299))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "crosscheck?":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
'''
port = 5299			
# connect to the server on local computer
s.connect(('127.0.0.1', port))
s.sendall("Hello Server".encode())

msg = input("Send your message:")
s.sendall(msg.encode())

def mul_msg(Num):
    while(Num):
        msgs = input("Enter your message:")
        s.sendall(msgs.encode())

Num = int(input("Enter the number of messages you want to send:"))
s.sendall(Num)
mul_msg(Num)




# receive data from the server and decoding to get the string.
#print (s.recv(1024).decode())
# close the connection

s.close()	
	
'''
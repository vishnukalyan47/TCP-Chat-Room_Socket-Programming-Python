from pydoc import cli
from re import T
import socket as soc
import threading			

s = soc.socket()		
print ("Socket successfully created")

port = 5299		

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen()	
#print ("socket is listening")

nickname = []
clients = []

def all_clients(message):
	for i in clients:
		i.send(message)

# Client A to Server to Client B
def msg_broker(client):
    while True:
        message = client.recv(1024) #Message from client.
        all_clients(message)


# Main Function to receive the clients connection
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = s.accept()
        print(f'connection is established with {str(address)}')
        client.send('crosscheck?'.encode('utf-8'))
        nn = client.recv(1024) 
        nickname.append(nn)
        clients.append(client)
        print(f'The nickname of this client is {nn}'.encode('utf-8')) #To display a new user in the server.
        all_clients(f'{nn} has connected to the chat room'.encode('utf-8')) 
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=msg_broker, args=(client,))
        thread.start()
if __name__ == "__main__":
    receive()
'''
while True:
	
# Establish connection with client.
	cli_con, cli_addr = s.accept()	
	print ('Got connection from', cli_addr )

	print (cli_con.recv(1024).decode())
	print (cli_con.recv(1024).decode())
	number = cli_con.recv(1024).decode()

	while(number):
		print (cli_con.recv(1024).decode())

# send a thank you message to the client. encoding to send byte type.
#cli_con.send('Thank you for connecting'.encode())

# Close the connection with the client
	cli_con.close()

# Breaking once connection closed
	break

'''
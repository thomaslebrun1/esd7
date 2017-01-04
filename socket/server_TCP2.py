import socket
import threading

bind_ip = "0.0.0.0" # local IP
bind_port = 8091   # port that you're locking for

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating object
server.bind((bind_ip,bind_port))  #bind called 
server.listen(5)  # 5 connections possible

print "[*] listening on %s:%d" %(bind_ip,bind_port) # say hi !

# client handle thread
def handle_client(client_socket):
	#print the client data
	while 1 :
		print ("cool say ?")
		while not raw_input:
			print("test2")
			request = client_socket.recv(4096)
			print "[*] Received: %s" % request
			print("test3")
		response = raw_input()
		client_socket.send(response)
		print("test3")



	client_socket.close()

while True: #loop for waiting connections
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
# threading started

	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
	
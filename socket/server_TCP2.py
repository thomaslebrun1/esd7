import socket
import threading

bind_ip = "0.0.0.0" # local IP
bind_port = 8088    # port that you're locking for

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating object
server.bind((bind_ip,bind_port))  #bind called 
server.listen(5)  # 5 connections possible

print "[*] listening on %s:%d" %(bind_ip,bind_port) # say hi !

# client handle thread
def handle_client(client_socket):
	#print the client data
	while 1 :
		print ("cool say ?")
		request = "0"
		response = "0"
		print ("test15")
		while (request=="0" and response=="0"):
			print("test")

			response = raw_input("flood")
			print("tes4")
			request = client_socket.recv(4096)
			print("tes5")

		print ("test155")
		if response <> 1 :
			print ("test1")
			client_socket.send(response)
		else :
			print "[*] Received: %s" % request
			print ("test2")
				#send back the packet

	client_socket.close()

while True: #loop for waiting connections
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
# threading started

	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
	
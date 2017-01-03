import socket

    # target
target_host = "127.0.0.1"
target_port = 8088

    # create the socket object with python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server on 80
client.connect((target_host,target_port))

while 1:
     # send some data to the server
     print ("Wanna say ?")
     request = "0"
     response = "0"
     while (request == "0" and response == "0"):
         request = raw_input()
         response = client.recv(4096)
         break
     print ("test2")
     if response <> 1:
         print ("test1")
         print response
     else :
         print ("test2")
         client.send(request)

     # print the response


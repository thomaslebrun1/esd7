import socket

    # target
target_host = "127.0.0.1"
target_port = 8091

    # create the socket object with python
# send some data to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server on 80
client.connect((target_host, target_port))

while 1:

    while not raw_input:

         print ("test1")
         response = client.recv(4096)
         print(response)
         print ("test2")
    request = raw_input()
    print ("test3")
    client.send(request)




     # print the response


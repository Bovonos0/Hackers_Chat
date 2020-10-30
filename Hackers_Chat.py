import socket
import os
import sys
import time
from datetime import datetime
#time
today = datetime.today()
day = today.strftime("%A")
month = today.strftime("%B")
year = today.strftime("%Y")
timy = today.strftime("%R")
#end time
#dbs
db_1 = ("1")
db_2 = ("2")
db_0 = ("0")
db_ecit = ("exit")
#end dbs
os.system("clear")
print ("Date = " + day,month,year,timy)

time.sleep(0.5)
print ("Welcome To Hackers Chat")
time.sleep(0.5)
print ("By Bovonos")
time.sleep(0.5)
txt = ".txt"
print ("git hub: https://github.com/Bovonos0")
print (" ")
print ("[1] Login")
print ("[2] Make a accound")
print ("[0] Exit")
user = input("choose: ")
if user== db_1:
    email = input("Email: ")
    passw = input("Password: ")
    passopen = open("account.txt",'r')
    data=passopen.read()
    if passw in data:
        print ("correct...")
        time.sleep(2)
        host = input ("set HOST: ")
        port = input ("set PORT: ")
        def lissen(host,port):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((host,port))
            if socket.error:
                print ("[-] Faild Connecting [-]")
            else:
                print ("[+] Connected Successfully [+]")
                def Successfully(host,port):
                    while True:
                        massage = input("Type Maasage: ")
                        if massage== db_exit:
                            os.system("exit")
    else:
        print ("incorrect...")


if user== db_2:
    email = input("Email: ")
    passw = input("Password: ")
    passsave = open("account.txt",'w')
    passsave.write(email+"\n"+passw)
    passsave.close()
    
if user== db_0:
    os.system("exit")
lissen(host,port)
Successfully(host,port)
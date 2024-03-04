from flask import Flask
from flask import request
from socket import *
from datetime import datetime

serversocket = socket (AF_INET, SOCK_DGRAM)
serversocket.bind(('', 53533))
print ("The server is ready to receive")
while True:
   message, clientAddress = serversocket.recvfrom (2048)
   modifiedMessage = message. decode () 
   print (modifiedMessage)

   if 'VALUE' in modifiedMessage:
      f = open("fibonacci", "a")
      f.write(modifiedMessage)
      f.close()
      
   else:
      f = open("fibonacci", "r") 
      response_f = f.read()
    #   print("Response", f.read())
      
      serversocket.sendto (response_f.encode (),clientAddress)
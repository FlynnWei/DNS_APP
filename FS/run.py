from flask import Flask
from flask import request
from socket import *
from datetime import datetime
app = Flask(__name__)


@app.route('/register')
def register():
    print('hello')
    serverName = 'localhost'
    serverPort = 53533
    clientSocket = socket (AF_INET, SOCK_DGRAM)
    message = 'TYPE=A NAME=fibonacci.com VALUE=0.0.0.0 TTL=10'
    clientSocket.sendto (message.encode () , (serverName, serverPort) )
    modifiedMessage, serverAddress = clientSocket.recvfrom (2048)
    
    clientSocket.close ()
   
   
@app.route('/fibonacci')
def fibonacci():
    print("f")
    number = request.args.get('number')

    def Fibonacci_Loop_tool(n):
        a,b = 0,1
        while n>0:
            a,b=b,a+b
            n -= 1

    def Fibonacci_Loop(n):
        result_list = []
        a,b = 0,1
        while n>0:
            result_list.append(b)
            a,b = b,a+b
            n -= 1
        return result_list


    return Fibonacci_Loop(int(number))


app.run(host='0.0.0.0',
        port=9090,
        debug=True)
from flask import Flask
from flask import request
from datetime import datetime
from socket import *
import re
import requests

app = Flask(__name__)


@app.route('/fibonacci')
def current_time():
    print("HEllo")
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if hostname is None or fs_port is None or number is None or as_ip is None or as_port is None:
        return "Record not found", 400
    
    # Send DNS Query
    serverName = '0.0.0.0'
    serverPort = 53533
    clientSocket = socket (AF_INET, SOCK_DGRAM)
    message = 'TYPE=A NAME=fibonacci.com'
    clientSocket.sendto (message.encode () , (serverName, serverPort) )
    modifiedMessage, serverAddress = clientSocket.recvfrom (2048)
    print(modifiedMessage.decode())
    clientSocket.close ()

    print(modifiedMessage.decode())
    

    fs_ip = re.findall(r'VALUE=(.*) ', modifiedMessage.decode())[0]
    print(fs_ip)
    fs_ip="0.0.0.0"
    
    r = requests.get(f"http://{fs_ip}:{fs_port}/fibonacci?number={number}")


    return r.text


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
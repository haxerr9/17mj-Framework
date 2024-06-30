# Script Made By 17mj
# -------------------
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import configparser

config = configparser.ConfigParser()
config.read(r'config.ini')

def ftpServer():
    path = os.getcwd()
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", path, perm="elradfmw")


    handler = FTPHandler
    handler.authorizer = authorizer

    address = (f"{config['DATABASE']['lhost']}", 21)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

ftpServer()
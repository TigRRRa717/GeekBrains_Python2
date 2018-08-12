import socket
import json

import time

def get_user(name, status):
    return {
        "account_name": name,
        "status": status
    }


def get_presence_message(user):
    return {

        "action": "presence",
        "time": time.time(),
        "user": user
    }

def format_message(dict_message):
    return json.dumps(dict_message).encode("utf-8")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 7777))

user = input("Input username: ")
status = input("Input status: ")

sock.send(format_message(get_presence_message(get_user(user, status))))
data_encode = sock.recv(1024)
print(data_encode.decode("utf-8"))

sock.close()
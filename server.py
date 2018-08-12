import socket
import json

OK = {
    "response": 200
}

BAD_REQUEST = {
    "response": 400
}

def get_response_on_message(data):
    if data["action"] == "presence":
        return json.dumps(OK).encode("utf-8")
    else:
        return json.dumps(BAD_REQUEST).encode("utf-8")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('', 7777))
server_socket.listen(5)

while True:
    sock, addr = server_socket.accept()
    while True:
        buf = sock.recv(1024)
        if not buf:
            continue

        buf = json.loads(buf.decode("utf-8"))

        print(buf)

        sock.send(get_response_on_message(buf))

    data_json = json.dumps(message)
    data_encode = data_json.encode()
    sock.send(data_encode)
    sock.close()

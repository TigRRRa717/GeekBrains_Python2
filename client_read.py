import socket
import utils

with utils.create_tcp_client("localhost", utils.PORT) as s:
    while True:
        msg = s.recv(1024)
        print(utils.convert_bytes_to_str(msg))


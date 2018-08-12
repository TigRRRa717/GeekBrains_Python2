import socket
import utils
import jim

with utils.create_tcp_client("localhost", utils.PORT) as s:
    # while True:
        s.send(utils.convert_str_to_bytes(jim.get_presence_message("Guest", "I'm online!")))


import time
import json
from pytest import raises
import socket
from client import get_presence_message, format_message

class UsernameToLongError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('Имя пользователя {} должно быть менее 26 символов'.format(self.name))

# МОДУЛЬНЫЕ ТЕСТЫ
def test_create_presence():
    # без параметров
    message = get_presence_message()
    assert message['action'] == "presence"
    # берем разницу во времени
    assert abs(message['time'] - time.time()) < 0.1
    assert message["user"]["account_name"] == 'Guest'
    # с именем
    message = get_presence_message('test_user_name')
    assert message["user"]["account_name"] == 'test_user_name'
    # неверный тип
    with raises(TypeError):
        get_presence_message(200)
    with raises(TypeError):
        get_presence_message(None)
    # Имя пользователя слишком длинное
    with raises(UsernameToLongError):
        get_presence_message('11111111111111111111111111')


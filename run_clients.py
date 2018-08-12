from subprocess import Popen, CREATE_NEW_CONSOLE

for i in range(5):
    Popen('python client.py localhost 7777 r', creationflags=CREATE_NEW_CONSOLE)

# input('Enter to exit from Python script...')
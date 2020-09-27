#basic irc bot
#08/02/2020
#joins a channel and prints out the output

import socket

server = "chat.freenode.net"
port = 6667
channel = "#testchan"
nick = "testbot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

irc.send(bytes("USER %s 0 * :test bot!\r\n" % nick, "UTF-8")) #user authentication
irc.send(bytes("NICK %s \r\n" % nick, "UTF-8"))       #sets nickname
irc.send(bytes("JOIN %s \r\n" % channel, "UTF-8"))   #join the channel

while True:
    lines = irc.recv(4096).decode('utf-8') #keep receiving data
    print(lines.rstrip()) #remove the blank new lines
    if (lines.find("PING") != -1): #simple ping response
        pong = "PONG " + lines.split(':')[1] + "\r\n"
        print(pong.rstrip())
        irc.send(bytes(pong, "UTF-8"))

irc.close()

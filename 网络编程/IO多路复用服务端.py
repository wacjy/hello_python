import socket
import select

server = socket.socket()
server.socketopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)

input_list = [server]

res = select.select(input_list,[],[])

import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.setblocking(False) # 设置阻塞 所有的网络阻塞都会变成非阻塞

server.listen(5)
c_list = []
d_list = []
while True:
    try:
        conn,addr = server.accept()
        c_list.append(conn)


    except BlockingIOError:
        print('没人来，干点其他事情')
        print('客户端数量',len(c_list))
        for conn in c_list:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    d_list.remove(conn)
                conn.send(data.upper())

            except BlockingIOError:
                pass
            except ConnectionResetError:
                conn.close()
                d_list.append(conn)

        for conn in d_list:
            c_list.remove(conn)

        d_list.clear()

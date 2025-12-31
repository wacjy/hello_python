import socket
import subprocess

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('127.0.0.1',8080))
server.listen(5)
while True:
    conn,addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
        except:
            break
        if not cmd:
            break
        obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out_res = obj.stdout.read()
        err_res = obj.stderr.read()
        data_size = len(out_res)+len(err_res) # 数据长度
        header = bytes(str(data_size),'utf-8').zfill(8) # 是后面长度的描述信息
        

        conn.send(header)
        conn.send(out_res)
        conn.send(err_res)


conn.close()


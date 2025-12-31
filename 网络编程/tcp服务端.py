import socket
from multiprocessing import Process

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8001))
s.listen(5)
def task(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except:
            break
    conn.close()

if __name__ == '__main__':

    while True:
        conn,addr = s.accept()
        # 通讯循环
        p = Process(target = task,args=(conn,))
        p.start()


        

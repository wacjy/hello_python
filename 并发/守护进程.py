from multiprocessing import Process,JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(8):
        time.sleep(random.randint(1,2))
        print(f'{name}生产了{food}{i}')
        q.put(f'{food}{i}')


    

def consumer(name,q):
    while True:
        food = q.get()
        time.sleep(random.randint(0,1))
        print(f'{name}吃了{food}')
        q.task_done()


if __name__ ==  '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer,args=('中华小当家','炒饭',q))
    p2 = Process(target=producer,args=('神厨小福贵','佛跳墙',q))
    c1 = Process(target=consumer,args = ('八戒',q))
    c2 = Process(target=consumer,args=('悟空',q))
    p1.start()
    p2.start()
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()

    q.join()
    print("主进程继续执行")

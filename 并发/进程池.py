from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import time
import os
pool = ProcessPoolExecutor()

def task(name):
    print(name,os.getpid())
    time.sleep(1)
    return name+10

def call_back(res):
    print('call_back',res)

if __name__ == '__main__':
    for i in range(50):
        future = pool.submit(task,'aa1').add_done_callback(call_back)   



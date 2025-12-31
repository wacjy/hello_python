import time
def f1():
    n = 0
    for i in range(100000000):
        n+=i
        yield

def f2():
    g = f1() # 得到f1生成器

    n = 0
    for i in range(100000000):
        n+=i
        next(g)


start = time.time()



f2()

end = time.time()
print(end - start)




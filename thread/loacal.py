import threading


lv = threading.local()
num = 0

def worker():
    global num
    num += 1
    lv.x = num
    print(lv)
    print(id(lv.x))
    print(lv.__dict__)
    print(dir(lv))


t1 = threading.Thread(target=worker)
t1.start()
t2 = threading.Thread(target=worker)
t2.start()

print(id(1), id(1), id(2),id(2),id(4), id(4))
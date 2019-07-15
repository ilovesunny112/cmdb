import threading
import time

a = threading.local()

def worker():
    a.x = 0
    for i in range(100):
        time.sleep(0.001)
        a.x += 1
    print(threading.current_thread(), a.x)
    print(a.__dict__)


for i in range(10):
    threading.Thread(target=worker).start()
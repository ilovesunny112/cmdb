
import threading
import time

def add(x, y):
    print(x + y)

t = threading.Timer(5, add, args=(4,5) )

t.start()

print(threading.enumerate())
time.sleep(2)
t.cancel()
time.sleep(0.0001)


print(threading.enumerate())

import threading
import time
import logging

logging.basicConfig(level=logging.INFO)


def worker():
    for i in range(1000):
        msg = "{} is running".format(threading.current_thread())
        logging.info(msg)
        t = threading.Thread(target=worker1, name="worker1-{}".format(i), daemon=True)
        t.start()


def worker1():
    for x in range(1000):
        msg = "$$$${} is running".format(threading.current_thread())
        logging.info(msg)


t = threading.Thread(target=worker, daemon=True, name="worker1-{}".format(0))

t.start()
t.join()


print("ending in main thread")
print(threading.enumerate())































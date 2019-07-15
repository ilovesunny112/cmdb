import threading
import time
import logging

logging.basicConfig(level=logging.INFO)

# def worker():
#     threading_obj = threading.current_thread()
#
#     for x in range(1000000):
#         # time.sleep(0.02)
#         msg = "{} started {} loop".format(threading_obj.name, x)
#         logging.info(msg)

num = 0

def worker():
    for x in range(1000):
        t = threading.Thread(target=worker1, name=x, daemon=False)
        t.start()



def worker1():
    global num
    for x in range(1000):
        num += 1
        logging.info("{}, {}".format(threading.current_thread(), x))
        # print("{} 次".format(num))

t1 = threading.Thread(target=worker, name="t1", daemon=True)


t1.start()
t1.join()

print(threading.enumerate())
print("main thread end", threading.current_thread())


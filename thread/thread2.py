import threading

def worker1():
    for i in range(10):
        print("{}-{} is online @ {}".format(threading.current_thread(), i, threading.current_thread().ident))


def worker():
    t1 = threading.Thread(target=worker1, name="w2", daemon=False)
    t1.start()
    # t1.setDaemon(True)
    for i in range(10):
        print("{}-{} is online @ {}".format(threading.current_thread(), i, threading.current_thread().ident))


t = threading.Thread(target=worker, name="w1", daemon=True)
t.start()

print("ending")
print("ending2")
print("ending")
print("ending2")
print("ending")


import threading
import logging


logging.basicConfig(level=logging.INFO)


def worker():
    name = threading.current_thread().name
    main_name = threading.main_thread().name
    for x in range(1000):
        msg = "thread {} started for {}, but main thread is {}\n".format(name, x, main_name)
        # print(msg, end="")
        logging.info(msg)


for _ in range(5):
    threading.Thread(target=worker, name="worker-{}".format(_),  daemon=True).start()

threading.Thread(target=worker, name="worker-{}".format(9),  daemon=False).start()

print("main ending")
print(threading.enumerate())
print(threading.active_count())

import threading
import time
import logging

FORMAT = "%(asctime)s %(thread)d %(message)s %(schoolname)s"

d = {"schoolname" : "HEBUT"}

logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%d-%H:%M:%S", filename="d:\\test.log", filemode="a" )

def add(x, y):
    logging.info("{} {}".format(threading.enumerate(), x + y), extra=d)

t = threading.Timer(5, add, args=(4,5),)



t.start()

print(threading.enumerate())
# time.sleep(2)
# t.cancel()
time.sleep(0.0001)
logging.warning("警告警告", extra=d)
logging.debug("调试信息", extra=d)
# logging.info("%(module)s")

print(threading.enumerate())
log = logging.getLogger("a.b")

print(log.name)
print(log, type(log))
log.info("aaa", extra = d)
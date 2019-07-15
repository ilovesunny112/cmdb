<<<<<<< HEAD


if __name__ == "__main__":
    print("welcome magedu")
=======
from dispatcher import Dispatcher

if __name__ == "__main__":
    print("welcome to my app")
    # 完成分发器功能

    dis = Dispatcher()
    dis.reg("cmd1", lambda :print("cmd1"))
    dis.reg("cmd2", lambda :print("cmd2"))

    dis.run()
>>>>>>> 8d006605dab523635113137cfdf0d76b6c28f31f

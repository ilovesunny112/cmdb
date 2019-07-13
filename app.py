from dispatcher import Dispatcher

if __name__ == "__main__":
    print("welcome to my app")

    dis = Dispatcher()
    dis.reg("cmd1", lambda :print("cmd1"))
    dis.reg("cmd2", lambda :print("cmd2"))

    dis.run()
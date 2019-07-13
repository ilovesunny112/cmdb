class Dispatcher:

    cmds = {}


    def reg(self, cmd, fn):
        self.cmds[cmd] = fn

    def run(self):
        while True:
            cmd = input("please input your commond\r\n").strip()
            if cmd == "quit":
                return
            fn = self.cmds.get(cmd, self.defaultfn)
            fn()

    def defaultfn(self):
        print("commond not found")
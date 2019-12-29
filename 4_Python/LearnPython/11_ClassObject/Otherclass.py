class MyNewRouter(MyRouter):
    def __int__(self,routername, model, serialno, ios, portsno):
        MyRouter.__init__(self,routername, model, serialno, ios)
        self.portsno = portsno

    def print_router(self, string):
        print(string , self.model)

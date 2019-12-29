class MyRouter(object):
    "This class desc characsteric of router"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print(" router ", self.routername)
        print(" model ", self.model)
        print(" serialno ", self.serialno)
        print(" ios ", self.ios)
        print(" model + manu_date ", self.model + manuf_date)
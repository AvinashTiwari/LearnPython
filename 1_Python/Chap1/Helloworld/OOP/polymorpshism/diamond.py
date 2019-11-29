class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(B):
    pass

class D(B,C):
    pass

d = D()
d.method()

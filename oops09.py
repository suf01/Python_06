class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, add):
        self.add = add

class C(A, B):
    def __init__(self, name, add):
        A.__init__(self, name)
        B.__init__(self, add)
    
obj = C("tom", "us")
print(obj.add)

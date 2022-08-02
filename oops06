# encapsulation

# protected -> derived can access base protected variables _
# private -> derived cannot access base private variables __

class example:
    __val = 10
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_data(self):
        print(f"x = {self.x}, y = {self.y}, private : {self.__val}")
    
e1 = example(1, 2)
e1.get_data()

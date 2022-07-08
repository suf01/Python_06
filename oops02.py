class entity:
    val = 100
    num_const = 11

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getdata(self):
        print(f'x = {self.x}, y = {self.y}, class variable value = {self.val}, constant val = {entity.num_const}')


e1 = entity(2, 4)
e1.val = 101
e2 = entity(5, 10)
e2.val = 201

e1.getdata()
e2.getdata()

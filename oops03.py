class entity:
    val = 100
    num_const = 11

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getdata(self):
        print(f'x = {self.x}, y = {self.y}, class variable value = {self.val}, constant val = {entity.num_const}')

    @classmethod
    def set_val(cls, value):
        cls.num_const = value

    # as an alternate constructor
    @classmethod
    def create(cls, x):
        a = int(x[0])
        b = int(x[1])

        return cls(a, b)

    @staticmethod
    def function(y):
        if y == 0:
            return False
        else:
            return True

e1 = entity(2, 4)
e1.val = 101
e2 = entity(5, 10)
e2.val = 201

entity.set_val(55)
e1.getdata()
e2.getdata()

x1 = ["2", "4"]
e3 = entity.create(x1)
e3.getdata()

print(entity.function(1))
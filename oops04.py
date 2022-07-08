class entity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getdata(self):
        print(f"x = {self.x}, y = {self.y}")


class more_entity(entity):
    def __init__(self, x, y, pos):
        super().__init__(x, y)
        self.pos = pos


e1 = entity(2, 4)
e2 = entity()

e3 = more_entity(1, 2, 3)
print(e3.x, e3.y, e3.pos)

print(isinstance(e3, more_entity))
print(issubclass(more_entity, entity))

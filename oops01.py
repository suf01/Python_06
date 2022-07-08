class entity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getdata(self):
        print(f"x = {self.x}, y = {self.y}")


e1 = entity(2, 4)
e2 = entity()

e1.getdata()
entity.getdata(e1)

e2.getdata()
entity.getdata(e2)

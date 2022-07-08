# method overriding
class base:
    def show_message(self):
        print("This is base class")


class derived(base):
    def show_message(self):
        print("This is derived class")

obj1 = derived()
obj1.show_message()

# method overloading
class entity:
    def add(self, x = None, y = None):
        if x!=None and y!=None:
            print(x+y)
        else:
            print(x)

e = entity()
e.add(1,2)
e.add(6)

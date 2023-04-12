# class1.py
class Person:
    def __init__(self):
        self.name = "decault name"

    def print(self):
        print("may name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

Person.title = "new title"

print(p1.title)
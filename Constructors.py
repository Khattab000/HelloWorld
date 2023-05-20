class Point:
    def __init__(self, x, y):     #self is the current object and __init__ is a constructor to enable to give the object values outside of its class
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def kill(self):
        print("attack")


point = Point(20, 30)  # it works just like parameters and keyword arguments
point.x = 10 # can also be updated
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print (f"Hello there, my name is {self.name}") # use always self as a reference to the object


Jason = Person('Jason') #Jason is a Object
Jason.talk()
print(Jason.name)

Bob = Person(" Bob Timothy")
Bob.talk()
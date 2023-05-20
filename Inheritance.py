# mechanism for reusing code like giving another class the same methods , try to not repeat yourself
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass    # pass is making python skip or pass the line bc python doesnt allow or like empty classes thats why we need to at least type in pass


class Cat(Mammal):
    def sound(self):      # you can also add methods that only the cat for example can use with addition of the inherited Methods
        print("miau")

Husky = Dog()
Husky.walk()

Kitten = Cat()
Kitten.walk()
Kitten.sound()
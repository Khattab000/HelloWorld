# classes are used to model new types that are more complex then the existing type we have here like list, dictionaries, numbers and so on
class Point:                    # we use Capital letters at the beginning of theword if we name Classes and unlike other things like list and dictionarys we dont use underscores to seperate words we just give both words Capital letters for Example EmailClient thats called the pascal naming convention
    def move(self):   # these are methods that the class that we created can use
        print('move')

    def kill(self):
        print("attack")


point1 = Point()  # point1 is an object that gets the class of point
point1.x = 10
point1.y = 20
point1.kill()
print(point1.x)
# the x or y attributes that point 1 has dont translate over to point2's attributes
point2 = Point()
point2.y = 1
print(point2.y)




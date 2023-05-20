# look at the python 3 module index for more information built in modules in python
# random is a built in module in python and it stored in the Python library root
import random

for i in range(3):
    print(random.random())   # the first random is the object and the second random is the function
                             # and the default random genrator only gives you numbers from 0 to 1 including bolean values
for i in range(3):
    print(random.randint(10, 20)) # for randint you need to specify two numbers to pick for example from 10 to 20 but that one uses only int

members = ['John', 'Mary', 'Joseph', 'Gilbert']
leader = random.choice(members)                  # random.choice for lists of people or items for example used for str
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second    # pycharm automatically interprets that as a tuple


dice = Dice()
print(dice.roll())




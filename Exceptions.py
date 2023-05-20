# we use that to handle errors, for example if someone uses a letter instead of a number in this code
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print(' Your age cant be lower or equal to zero')

except ValueError:
    print("Age has to be a numerical Value")






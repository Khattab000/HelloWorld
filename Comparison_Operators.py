# == (that value)
# != (not that value)
# <=
# >=
# temperature = 30

if temperature == 30:
    print("it's a hot day")
else:
    print("it's a lovely day")

letter_count = input("Please enter your Name ! ")
if len(letter_count) < 3:
    print(" Name is too short, your name has to be at least 3 characters long")
elif len(letter_count) > 50:
    print("Name is too long, your Name can't be longer then 50 Characters !")
else:
    print("Name looks good.")


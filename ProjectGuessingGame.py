secret_number = 9
tries = 0
guess_limit = 3
print("Guess the secret Number between 0 - 10 , you only have 3 Tries ")
while tries < guess_limit:
    guess = int(input("Guess : "))
    tries+=1
    if guess == secret_number:
        print("you won !!!!")
        break
else:
    print("You lost D:")






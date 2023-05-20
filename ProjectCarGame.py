command = ''
switch = 0
started = False
while True:
    command = input(">").lower()
    if command == "help":
        print('''
start - to start the car 
stop - to stop the car 
quit - to exit the game''')
    elif command == "start":
        if started:
            print("Car is already Moving ")
        else:
            print("Car started ... ready to go !!!")
            started = True
    elif command == "stop":
        if not started:
            print("the car already stopped")
        else:
            print("stopped the car")
            started = False

    elif command == 'quit':
        print("Thanks for playing my Game !!!")
        break
    else:
        print("I dont understand this, for more information type 'help' ")

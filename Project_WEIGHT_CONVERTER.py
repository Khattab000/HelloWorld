weight = int(input("Weight:"))
unit_of_measurement = input("(K)g or (L)bs:")
if weight >= 0 :
    if unit_of_measurement.upper()== "K":
        print(str(weight / 0.45) + ' lbs')
    if unit_of_measurement.upper() == 'L':
        print(str(weight * 0.45) + ' kg')
    else:
        print("Unit of measurement has to be either K or L")

else:
    print("Weight has to be a number and be at least 0 !")

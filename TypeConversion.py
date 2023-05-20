birth_year = input('Birth Year: ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print(str(age) + ' years')

weight = input('What is your weight in pounds ? ')
weight_in_kg = float(weight) / 2.205
print('your weight in kg is : ' + str(weight_in_kg))
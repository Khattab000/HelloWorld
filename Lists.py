names = ['John', 'Bob', 'Mosh', 'Sarah', 'Muffin']
names[0] = 'Jon'
print(names)

numbers = [3, 6, 2, 8, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
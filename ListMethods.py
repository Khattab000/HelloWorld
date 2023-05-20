numbers = [5, 2, 1, 1, 7, 4]
numbers.append(13)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(2))
print(1 in numbers)
print(numbers.count(1))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
numbers.clear()
print(numbers)

box = [2, 6, 3, 5, 3, 2, 9, 7, 8, 8]
for duplicate in box:
    if box.count(duplicate) > 1:
        box.remove(duplicate)
print(box)

oder = ''

nummer = [2, 6, 3, 5, 3, 2, 9, 7, 8, 8]
uniques = []
for numer in nummer:
    if numer not in uniques:
        uniques.append(numer)
print(uniques)

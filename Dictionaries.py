customer = {
  "name" : "John Smith",
    "age": 30,            # all of the dictionary values has to be unique for example you can't use age twice
    "is_verified": True
}
print(customer["name"])
print(customer.get("name", "Hohenheim"))
print(customer.get("birthday"))
print(customer.get("birthday" , "Hohenheim")) # if it doesn't find anything it uses the second one as a default value inestead of saying "none"
customer["name"] = 'Jeremiah Snow'
print(customer['name'])
customer['birthday'] = '01.03.1989'
print(customer)

phone = input("Phone: ")
numbers = {
    "0" : ' zero',
    "1" : ' one',
    "2" : ' two',
    "3" : 'three',
    "4" : 'four'
}
output = ""
for character in phone:
    output += numbers.get(character, "!") + ''
print(output)





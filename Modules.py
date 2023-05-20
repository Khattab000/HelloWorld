# modules are files with python code and these are split in sections just like in a supermarket and each file is called module it makes the code more structured and organized
# converter.py is used as a Module that means we can use the code of converters.py without needing to write it here and the code is much more structured

import converters
print(converters.kg_to_lbs(100))

from converters import lbs_to_kg  # this one is used to not import the whole module , just to take one specific thing like this function and with that we dont need to type out the name of the module with the function and only get the one thing we ask for
print(lbs_to_kg(100))

from converters import find_max   # small tip uses control and space to get the options of the available methods
numbers = [1,3,4,8,6]
max = find_max(numbers)     # look at converter.py as reference and actually this one is just a excersice bc the module was already fully importet there is no need to write it everytime
print(max)                  # btw the reason why max in line 12 has a yellow  underline is that python already has a in built max function and technically we are rewriting the function which is considered bad practice
                            # built in max function would look like this : print(max(numbers)) but it cant be used currently bc we have rewritten max
                            # you could rename it and use refractor (shift and F6) to rename every max but yeah you should avoid rewriting built in functions








# basically another way to organize our code especially for modules for example modules that are working together or meant for a specific task are put into one package
# example for package would be a mall that is split in Men, Women and Children Clothes each one of them is one package containing multiple modules
# right-click on the project and go to new, then press new directory and name it, after that you need to create a new python file with the name __init__.py so the directory is converted to a python package
#short cut that can be used in pycharm just right-click on the prject and go to new and then press new package that will automatically create the package including the __init__.py
# look at the "ecommerce" package for reference

import ecommerce.shipping    #we cant just import a function from a package we need to include the package name too
ecommerce.shipping.calculate_shipping()

# another way to shorten the code and not be force to type the package name every time you want to use the function
from ecommerce.shipping import calculate_shipping
calculate_shipping()

# if you want to import all functions of a model you can type this :
from ecommerce import shipping
shipping.calculate_shipping()

# if you want to add only certain modules you write ' from ecommerce.shipping import calculate_shipping, move_shipping'



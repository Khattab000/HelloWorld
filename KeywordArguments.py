def greet_user(title, last_name):
    print(f'Hi {title} {last_name} !')
    print('General Kenobi')


print('Start')
greet_user('John', 'Smith')  # these two are positional Arguments their Positions matters.
greet_user(last_name='John', title='Smith') # these are keyword Arguments their position doesnt matter can be useful especialy for numbers (if you mix positional and keyword arguments then you have to put the positional first then the keywords one)
print('Finish')

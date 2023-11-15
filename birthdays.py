'''The goal of this module is to define two functions to create a dictionary and 
understand the birthday of the celebreties'''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    '''Functions which returns the name of the celebrities prenest in the variable birthdays'''
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    '''Function which returns the name and the corrispant birthday'''
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

'''Let's see if everything works now'''
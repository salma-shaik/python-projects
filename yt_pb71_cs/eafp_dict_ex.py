person = {'name': 'Joe', 'age': '34', 'job': 'teacher'}
# person = {'name': 'Joe', 'age': '34'}

# LBYL - Non Pythonic
# if 'name' in person and 'age' in person and 'job' in person:
#     print('My name is {name}. I am {age} years old and I work as a {job}'.format(**person))
# else:
#     print('Missing some keys')


# EAFP - Pythonic
try:
    print('My name is {name}. I am {age} years old and I work as a {job}'.format(**person))
except KeyError as e:
    print('Missing {} key'.format(e))


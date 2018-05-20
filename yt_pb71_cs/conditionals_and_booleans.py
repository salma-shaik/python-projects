# if True:
#     print("Prints")
# if False:
#     print("doesn't print")
#
# language = "Python"
#
# if language == "Python":
#     print('Language is Python')
# elif language == "Java":
#     print('Language is Java')
# elif language == "JavaScript":
#     print('Language is Java Script')
# else:
#     print("No Match")

user = 'Admin'
#logged_in = True
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad User')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


#Object Equality
a = [1,2,3]
#b = [1,2,3]

b = a

print(id(a))
print(id(b))

print(a == b)
print(a is b)


#condition = False

#condition = None

#condition = 0

#condition = 10

#condition = []

#condition = ''

#condition = {}

#condition = ()

condition = 'test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
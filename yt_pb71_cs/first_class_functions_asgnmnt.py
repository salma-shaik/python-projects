'''
First class functions allow us to treat functions like any other object.
For ex we can pass functions as arguments to another function, pass functions as
arguments and return functions.
'''


def square(num):
    return num*num


# f = square(5)
# print(square)
# print(f)
#
# print()

# assigning function to a variable
square_var = square # no (). Coz if there are (), then the function will be executed
# print(square)
# print(square_var)


def cube(num):
    return num**3


cube_var = cube

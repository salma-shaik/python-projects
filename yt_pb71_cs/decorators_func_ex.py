'''
    A decorator is a function that takes another func as an arg, adds some kind of functionality
    and then returns another func without altering the source code of the original function
    that was passed in.
'''


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('Display function ran')


display()
# decorated_display = decorator_function(display)
# decorated_display()

print()


@decorator_function
def display_info(name, age):
    print(f"{name} is {age} years old")


display_info('John', 35)


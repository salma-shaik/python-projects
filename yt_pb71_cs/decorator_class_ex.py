class decorator_class(object):

    def __init__(self, original_function):
        # ties our function with the instance of this class
        self.original_function = original_function

    # behaves just like the wrapper function
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('Display function ran')


display()
# decorated_display = decorator_function(display)
# decorated_display()

print()


@decorator_class
def display_info(name, age):
    print(f"{name} is {age} years old")


display_info('John', 35)
def prefix_decorator(prefix):
    def decorator_function(prefix, original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed before', original_function.__name__)
            original_function(*args, **kwargs)
            print(prefix, 'Executed after', original_function.__name__)
        return wrapper_function
    return decorator_function


@prefix_decorator('MESSAGE: ')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Jacob', 34)



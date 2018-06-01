'''
A closure closes over the free variables from their environment.
Closures allow us to take advantage of first class functions and return
inner functions that remembers and has access to variables local to the scope
in which they were created.
Closure remembers the inner variable even after the outer function has finished executing
'''

import logging

logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x,y):
    return x+y


def sub(x,y):
    return x-y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 5)
sub_logger(6, 2)

add_logger(5, 5)
sub_logger(2, 6)

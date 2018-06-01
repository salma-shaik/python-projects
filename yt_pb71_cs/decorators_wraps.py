from functools import wraps


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def log_wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return log_wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def time_wrapper(*args, **kwargs):
        t1 = time.time()
        time.sleep(1)
        result = original_function(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in: {} sec'.format(original_function.__name__, t2))
        return result

    return time_wrapper


@my_logger
@my_timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 40)


import time


def my_time(original_function):
    def time_wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in: {} sec'.format(original_function.__name__, t2))
        return result
    return time_wrapper


@my_time
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Mark', 23)
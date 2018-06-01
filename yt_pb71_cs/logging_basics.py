import logging
import logging_emp_class

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler= logging.FileHandler('logging_basics.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename='logging_basics.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(name)s:%(message)s')


def add(x, y):
    """Add Function"""
    return x+y


def subtract(x, y):
    """Subtract Function"""
    return x-y


def multiply(x, y):
    """Multiply Function"""
    return x*y


def divide(x, y):
    """Divide Function"""
    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result


num1 = 20
num2 = 0

add_result = add(num1, num2)
# print(f'Add: {num1} + {num2} = {add_result}')
# logging.debug(f'Add: {num1} + {num2} = {add_result}')
logger.info(f'Add: {num1} + {num2} = {add_result}')
# logging.warning(f'Add: {num1} + {num2} = {add_result}')

subtract_result = subtract(num1, num2)
# print(f'Sub: {num1} - {num2} = {subtract_result}')
logger.debug(f'Sub: {num1} - {num2} = {subtract_result}')
# logging.warning(f'Sub: {num1} - {num2} = {subtract_result}')

multiply_result = multiply(num1, num2)
# print(f'Mul: {num1} * {num2} = {multiply_result}')
logger.debug(f'Mul: {num1} * {num2} = {multiply_result}')
# logging.warning(f'Mul: {num1} * {num2} = {multiply_result}')

divide_result = divide(num1, num2)
# print(f'Div: {num1} / {num2} = {divide_result}')
logger.debug(f'Div: {num1} / {num2} = {divide_result}')
# logging.warning(f'Div: {num1} / {num2} = {divide_result}')

from first_class_functions_asgnmnt import *

nums_list = [1, 2, 3, 4, 5]


# a higher order function which takes a function and an array of numbers as args
# here, we wil pass in a square func to which every num from the array is passed to be squared
def func_array_as_args(func, num_array):
    num_squares = []
    for num in num_array:
        num_squares.append(func(num))
    return num_squares

# passing in the square func
print(func_array_as_args(square_var, nums_list))

# passing in the cube function
print(func_array_as_args(cube_var, nums_list))


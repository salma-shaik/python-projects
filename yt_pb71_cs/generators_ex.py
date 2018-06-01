nums_list = [1, 2, 3, 4, 5]
nums_squares_list = []


def square_nums(list1):
    for num in list1:
        nums_squares_list.append(num*num)
    return nums_squares_list


# print(square_nums(nums_list))


# generator for squaring numbers
def square_nums_gen(list1):
    for num in list1:
        print("prints")
        yield num*num


# gen_squares = square_nums_gen(nums_list)

gen_squares = square_nums_gen(nums_list)

# iterating through generator list
for num in gen_squares:
    print(num)

# convert generator to list
# converting to list might have performance problems when we have large dataset
# to be held in memory with a list
# print(list(gen_squares))

# generators doesn't hold the objects in memory. just processes in time whatever we need.
# don't have to hold too  many objects in memory while looping as required by a list
# print(next(gen_squares))
# print(next(gen_squares))
# print(next(gen_squares))
# print(next(gen_squares))
# print(next(gen_squares))
# print(next(gen_squares))




# list comprehension
squares_comp = [x*x for x in nums_list]
# print(squares_comp)

# generator from comprehension
# squares_comp_gen = (x*x for x in nums_list)
# for num in squares_comp_gen:
#     print(num)

num_list = [1,2,3,4,5,6]
# num_list = [1, 2, 3, 4, 5]

# Non-pythonic
# if len(num_list) >= 6:
#     print(num_list[5])
# else:
#     print("Index out of bounds")

# Pythonic:
try:
    print(num_list[5])
except IndexError as e:
    print(e)

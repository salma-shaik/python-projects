num_list = [1, 2, 3, 4, 5]

# for i in num_list:
#     print(i)
#     # if i == 3:
#     if i == 6:
#         break
# else:
#     print ('Hit the For/Else Statement')

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print('Hit the For/Else Statement')


def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


names_list = ['Mary', 'Jane', 'Leo', 'Rick']

# index_location = find_index(names_list, 'Jane')

index_location = find_index(names_list, 'Amy')

print('Location of target is index: {}'.format(index_location))

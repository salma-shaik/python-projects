list1 = [9, 1, 8, 2, 7, 3, 6, 4, 5]

'''
s_list1 = sorted(list1, reverse=True)

print('Sorted: ', s_list1)

list1.sort(reverse=True)

print('Original: ', list1)


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
#print(tup.sort())
s_tup = sorted(tup)
print(s_tup)
'''

dict1 = {'name':'John', 'Age':32, 'User': True}
s_dict1 = sorted(dict1)
print(dict1)

list2 = [-6, -5, -4, 1, 2, 3]
# s_list2 = sorted(list2)
s_list2 = sorted(list2, key=abs)
print(s_list2)


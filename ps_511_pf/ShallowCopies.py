list1 = [[8,4],[3,90]]

list2 = list1[:]

"""
print(list2 is list1)
print(list2 == list1)

list1.append([5,0])

print(list2 is list1)
print(list2 == list1)

print(list1)

print(list2)

list2.append([23,8])

print(list1)

print(list2)

"""

list1[1] = [99,100]

print(list1)

print(list2)

list1[0].append(34)

print(list1)

print(list2)

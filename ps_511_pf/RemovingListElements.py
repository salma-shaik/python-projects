w = "The great journey to the center of the universe"

list1 = w.split()

del list1[3]

print(list1)

list1.remove('the')

print(list1)

list1.remove('journey')

print(list1)

del list1[list1.index('center')]

print(list1)

list1.remove(list1[list1.index('great')])

print(list1)

list1.insert(1,'mystery')

print(list1)

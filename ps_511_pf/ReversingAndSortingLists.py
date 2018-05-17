list1 = [43,53,23,76,2]

list1.reverse()

print(list1)

list1.sort()

print(list1)

list1.sort(reverse=True)

print(list1)


s1 = "it was a season of hope, it was a season of despair"

list2 = s1.split()

print(list2)

print(' '.join(list2))

list2.sort()

print(list2)

list2.sort(key=len)

print(list2)

p = [5,9,23,76,6]

q = sorted(p)

print(q is p)

q1 = reversed(p)

print(q1 is p)
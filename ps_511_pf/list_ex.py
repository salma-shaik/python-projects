s = "show how to do index into sequences".split()

"""
print(s)

print(s[4])

print(s[-1])

print(s[-0])

print(s[1:4])

print(s[1:-1])

print(s[3:])

print(s[:3])

print(s[:])
"""

"""
s1 = s[:]
print(s1==s)

s1.append(43)

print(s)
print(s1)

s.append(90)
print(s1)
print(s)
"""

list1 = s.copy()
print(list1 )


list2 = list(s)
print(list2)

print(list2 is s)

print(list2 == s)

list2.append(45)

print(list2)
print(s)



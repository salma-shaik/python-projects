"""
tup_obj = ("Norway", 345, 234.0, 'Y')

print(tup_obj[0])
print(tup_obj[2])

print(len(tup_obj))


for item in tup_obj:
    print(item)


print(tup_obj + (234, 'werwer', 'bthtybnh'))

print(tup_obj*2)

nested_tup = ((23,43), (45,6), (43,35))

print(nested_tup[1][1])  # 6

h1 =(143)
print(type(h1))

h2 = (143,)
print(type(h2))


e = ()

print(type(e))


tup1 = 34,5,2,6

print(tup1)
print(type(tup1))



def minmax(tup):
    return min(tup), max(tup)


print(minmax([34,56,2,7,8]))

lower, upper = minmax([34,56,2,7,8])

print(lower)
print(upper)

(a,(b,c,(d,e))) = (3,(8,9,(1,2)))

print(a,b,c,d,e)


(a,(b,c,(d,e))) = (3,("str",9,("test",2)))

print(a,b,c,d,e)

a = 'jelly'

b = 'bean'

c = 'choc'

a,b,c = c,a,b

print(a,b,c)

a,b,c = b,c,a

print(a,b,c)
"""

tup_from_list = tuple([43,5,2,7])
print(tup_from_list)

tup2 = tuple("immutable")
print(tup2)

print(5 in tup_from_list)

print(5 not in tup_from_list)
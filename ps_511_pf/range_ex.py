print(range(5))

range1 = range(5)

for i in range1:
    print(i)

print(list(range(5,10)))

print(list(range(2,5,1)))


tup = [8,234,6,23,64,756]

for i in enumerate(tup):
    print(i)


for i,v in enumerate(tup):
    print("i={}, v={}".format(i, v))


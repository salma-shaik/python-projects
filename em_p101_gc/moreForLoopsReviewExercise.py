str1 = "test"
intList=[2,4,3,45,23]
dict={1:"test",2:23,34:"test23"}

for char in range(len(str1)):
    print(str1[char])

print()

for int in intList:
    print(int,end=" ")

print()

for key in dict:
    print(str(dict[key]))

intList2=[34,2,3,24,23]

print()

for item1,item2 in zip(intList,intList2):
    if(item1>item2):
        print(item1)
    elif(item1<item2):
        print(item2)
    else:
        print(item1)


for int in intList:
    print(int,end=" ")
else:
    print(100)
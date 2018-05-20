nums = [1,2,3,4,5]

"""
for num in nums:
    if num == 3:
        print("Found it!")
        #break
        continue
    print(num)
"""

"""
#loop within a loop
for num in nums:
    for letter in 'abc':
        print(num,letter)
"""

#run through a loop for certain number of times
for i in range(1, 11):
    print(i)


#while loop
x = 0
while x<10:
    if x==5:
        break
    print(x)
    x += 1


#infinite loop
x = 0
while True:
    # if x==5:
    #     break
    print(x)
    x += 1



"""
0.Setup
a.create a list of 13 integers and assign it to a variable
"""

intList=[1,2,3,4,5,6,7,8,9,10,11,12,13]

"""
1.List Slicing With Stride
a.create a variable an assign it a list slice comprised of every 4th number from the list you made in step 0.a.
b.print the list slice from step 1.a.
"""

slicedIntList = intList[0:13:4]
print(slicedIntList)

"""
2.List Slicing with Stride and Omitted start and end indices
a.using only stride, assign a list slice composed of every 3rd value from the list you made in step 0.a. to a variable.
b.print the list slice from step 2.a.
"""

slicedIntList2 = intList[::3]
print(slicedIntList2)

"""
3.Reversing Lists with Stride
a.reverse the list you made in step 0.a. and assign it to a variable
b.print the reversed list you made in step 3.a.
"""

reverseIntList = intList[::-1]
print(reverseIntList)
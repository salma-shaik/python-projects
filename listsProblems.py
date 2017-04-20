"""
Creating A List and Accessing by Index:
1.create a 4 element list that consists of values that are all strings and assign it to a variable
2.create a 3 element list that consists of values that are all numbers and assign it to a variable
3.create a 5 element list that contains at least 1 string, 1 number, and 1 Boolean value and assign it to a variable
4.Print the list you created in step 1
5.Access by index and print the second element of the list you made in step 2
6.Access by index and print the the boolean value from the list you made in step 3
"""
# ----------------------------------------------------------------------------------------------------------------------

strList=["ghg","hjhi","sggvhb","klk"]
numList=[7,9,-8]
mixedList=["test",True,"test2",76,55]

print(strList)
print(numList[1])
print(mixedList[1])
# ----------------------------------------------------------------------------------------------------------------------
"""
Index Reassignment and .append():
1.create a variable and assign it the list [1, 2, 3]
2.reassign the first element in the list from step 1 the value 2
3.reassign the second element in the list from step 1 the value 3
4.reassign the third element in the list from step 1 the value 4
5.use .append() to add the value 6 to the end of the list from step 1
6.print the resulting list
"""
# ----------------------------------------------------------------------------------------------------------------------
numList2 = [1,2,3]
numList2[0]=2
numList2[1]=3
numList2[2]=4
numList2.append(6)

print(numList2)
# ----------------------------------------------------------------------------------------------------------------------
"""
List Slicing:
1.create a 7 element list and assign it to a variable
2.slice the list from its first element to its fourth element and print the resulting 4 element list
3.slice the list from its third element to its fifth element and print the resulting 3 element list
4.slice the list from its second element to its last element and print the resulting 6 element list
"""
# ----------------------------------------------------------------------------------------------------------------------
sliceEx=[324,23,1,2,343,21,2]
sliceEx1=sliceEx[:4]
print(sliceEx1)

sliceEx2=sliceEx[2:5]
print(sliceEx2)

sliceEx3=sliceEx[1:]
print(sliceEx3)
# ----------------------------------------------------------------------------------------------------------------------
"""
.index() and .insert()
1.create a variable and assign it the list ["Bob Dylan", "Like a", "Rolling Stone"]
2.use the .index() function to find and print the index of the string "Rolling Stone" from the list in step 1
3.use the .insert() function to insert the string 1965 at index 0 of the list from step 1
4.print the list that results from step 3
"""
# ----------------------------------------------------------------------------------------------------------------------
strList=["Bob Dylan", "Like a", "Rolling Stone"]
print(strList.index("Rolling Stone"))
strList.insert(0,"1965")
print(strList)
# ----------------------------------------------------------------------------------------------------------------------
"""
.remove() and .pop()
1.create a variable and assign it the list ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
2.use .remove() to remove of the "Sutcliffe" from the list created in step 1.
3.print the new list
4.use .pop() to remove and print "Lennon" from the list
5.use .pop() to remove and print "Harrison" from the list
6.print the new list
"""
# ----------------------------------------------------------------------------------------------------------------------
strList2=["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
strList2.remove("Sutcliffe")
print(strList2)
print(strList2.pop(1))
print(strList2.pop(2))
print(strList2)
# ----------------------------------------------------------------------------------------------------------------------
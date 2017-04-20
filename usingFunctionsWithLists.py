"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
"""

"""
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
"""

intList=[2,442,33,6,22,454,42]
strList=["test1","abc","test2"]
floatList=[23.43,2.343,21.4]


"""
2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
"""
def takesParam(a):
    print(a)

takesParam(intList)
takesParam(strList)
takesParam(floatList)


"""
3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
"""

def prodOfList(li):
    prod=1
    for listElement in li:
        prod *= listElement
    return prod

print(prodOfList([2,3,4]))


def strConcat(li):
    str=""
    for listElem in li:
        str += listElem
    return str

print(strConcat(strList))


def quotient(c):
    print (c[ 2 ] / c[ 1 ])

quotient(floatList) # prints the quotient of 3.54 and 2.43

"""
4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
.index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""

def listManip(li):
    li.append("end")
    li.remove("abc")
    li.insert(2,"ins")
    print(li)

listManip(strList)



"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

def noParamPrintStr():
    print("Printing from no param constructor")


noParamPrintStr()

var5 = 5


def singleParamPrint(param):
    print(param)


singleParamPrint(5)

"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

var1 = 4
var2 = 7
var3 = 3948


def diffOfTwo(a, b):
    print(a - b)


def productOfThree(a, b, c):
    print(a * b * c)


diffOfTwo(var1, var2)
productOfThree(var1, var2, var3)

"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

float1 = 3.323
float2 = 54.233432
float3 = 31.23


def quoOfTwo(a, b):
    return a / b


def nestedQuo(a, b, c):
    return (quoOfTwo(a, b)) / c


quoOfTwoResult = quoOfTwo(float1, float2)
print(quoOfTwoResult)

print(nestedQuo(float1,float2,float3))

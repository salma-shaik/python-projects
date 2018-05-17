"""
1.Iterating through a string using range() and a for loop
a.create a string and assign it to a variable
b.use a for loop without a range() to iterate through and print the contents of the string from step 1.a.
c.use a for loop with a range() to iterate through and print the contents of the string from step 1.a.
"""

strVar = "test"

for char in strVar:
    print(char)

for char in range(len(strVar)):
    print(strVar[char])


"""
2.Using , and end to print output of a for loop on the same line
a.create a variable and assign it a list of integers
b.use a for loop with , and end to print all the integers from the list you made as one integer (eg if your list was
[1, 2, 5, 7], the output of the for loop should be 1257)
c.use a for loop with , and end to print all the integers from the list you made with "X" between them (eg if your list
was [4, 3, 2, 1], the output of the for loop should be 4X3X2X1X)
"""

intList = [2,3,45,324,31]

for int in intList:
    print(int,end="")

"""
3.Using a for loop to iterate through a dictionary
a.create a dictionary and assign it to a variable
b.use a for loop to iterate through the dictionary and print its keys and values with the following form:
value key (eg, if your dictionary is {"first": 1, "second": 2}, your output should be 1 "first" and on another line
2 "second")(since dictionaries don't have to print in order, your output with {"first": 1, "second": 2} as your
dictionary could have also been 2 "second" and on another line 1 "first")
"""

dict1={1:"one",2:"two","three":3}
for key in dict1:
    print()
    print(str(dict1[key]) +" " + str(key))


"""
4.zip()
a.create 2 lists of numbers and assign them to variables
b.use a for loop and zip() to iterate through both those lists, sum their values, and append those values to a new list
(eg, if one of your lists is [1, 2] and your other list is [5, 9], then the for loop would iterate through them,
add 1 to 5 resulting in 6 and add 2 to 9 resulting in 11)
c.print the new list (the resulting list from the example given in 4.b. would be [6, 11])
"""
list1=[4,4,345,55645,22,34,546]
list2=[5.3454,34,3.234,5.44,3454,5,234]
resList=[]

for li1,li2 in zip(list1,list2):
    resList.append(li1+li2)
print(resList)


"""
5.for/else
a.create a tuple with 5 elements that are all strings and assign it to a variable
b.create a for/else loop that prints the first 4 elements of the tuple from step 5.a. with its for loop portion and
the fifth element of the tuple from step 5.a. with the else statement
c.create a for/else loop that prints the first 3 elements of the tuple from step 5 then ends prematurely before the else
statement is triggered using a break statement
"""

tup1=("sdf","dsdsdf","d","asda","dwedw")
counter1=1
for str in tup1:
    if(counter1<5):
        print(str)
        counter1 += 1
else:
    print(tup1[4])

counter2=1
for str in tup1:
    if(counter2<4):
        print(str)
        counter2 += 1
    else:
        break
else:
    print(tup1[4])
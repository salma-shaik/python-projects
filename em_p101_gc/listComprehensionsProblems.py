"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
"""

list1=[num for num in range(8,-1,-2)]
print(list1)

list2=[num1**num1 for num1 in range(1,5)]
print(list2)

list3=[num2*(num2+2) for num2 in range(4,7)]
print(list3)


"""
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""

list1 = [num for num in range(2,10) if num!=5 and num!=6]
print(list1)

list2 = [num for num in range(10,0,-1) if num<4 or num>7]
print(list2)

list3 = [num for num in range(1,11,1) if num!=2 and num!=3 and num!= 7 and num!=8]
print(list3)
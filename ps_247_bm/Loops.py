student_names = ["John", "Mary", "Cara", "Bruno", "Dave", "Max", "Kim", "Don", "Tia"]

"""
for name in student_names:
    if name=="Dave":
        continue
        print("Found him: " +name)
        #break
    print("Currently testing: " +name)
"""

#Practice 2
for name in student_names:
    #print("Student name is {0}".format(name))
    #print(f"Student name is {name}")
    #print(name)
    print(name.title())

""" 
for index in range(10):
    print(index)

for index in range(4,10):
    print(index)

for index in range(5,10,2):
    print(index)


for name in student_names:
    if name == "Cara":
        #print("Found " + name)
        #break #breaks out of the loop
        continue #continues with the next iteration of the loop
        # Unreachable code
        print("Found " + name)
        print("This won't be printed")
    print("Tested: " + name)


#while loop

num = 6

while num != 9:
        print(num)
        num = num+1"""
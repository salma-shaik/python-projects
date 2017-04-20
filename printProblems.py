"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it.
helloWorld = "hello"+"world"
int11 = 11
int38 = 38
str1138 = str(int11)+str(int38)
print(helloWorld,int11,int38,str1138)
# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
[name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.
favRestaurant = input("What is your favorite restaurant?")
place = input("Which place do you want to visit?")
username=input("Please enter a nickname or firstname")
userInfo = "Your favorite restaurant is %s, you want to visit %s, \
and your nickname or first name is %s"%(favRestaurant,place,username)
print(userInfo)
print("I like %s"%"reading")

# ----------------------------------------------------------------------------------------------------------------------
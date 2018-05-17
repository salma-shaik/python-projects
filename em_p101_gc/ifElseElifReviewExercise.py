userName = input("Please enter your name")
usernameLength = len(userName)

if usernameLength<4:
    print("Your name is less than 4 characters")
elif usernameLength>=4 and usernameLength<10:
    print("Your name is atleast 4 characters and less than 10 characters")
else:
    print("your name is very long")

from random import randint

counter = 5

while counter<10:
    print(counter)
    if counter==7:
        print("counter value is 7")
        break
    else:
        counter = randint(5,10)
else:
    print("Counter is equal to 10")
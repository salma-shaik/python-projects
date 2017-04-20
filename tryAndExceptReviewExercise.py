from random import randint

int1 = input("please enter a number")
int2 = randint(0,5)
print(int2)

def compareTwo(a,b):
    try:
       # userInt = int(a)
        #print(userInt)
        if int(a) > b:
            print("a is greater %d" %int(a))
        elif int(a) < b:
            print("b is greater %d" %int(b))
        else:
            print("both are equal")
    except:
        print("please enter a valid integer")

compareTwo(int1,int2)
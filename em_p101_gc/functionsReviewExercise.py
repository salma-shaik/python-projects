#Step 1
def noParam():
    print("this is a function")

#Step 2
def multInt(a):
    return a*2

#Step 3
def multTwoInts(a,b):
    return a*b

#Step 4
def threeParams(a,b,c):
    print(multTwoInts(multInt(a),b)*c)

noParam()
threeParams(7,4,2)



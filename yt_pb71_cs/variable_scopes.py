'''
L- Local
E - Enclosing
G - Global - @ top level of module; explicitly defined using 'global' keyword
B - Built-in
'''

import builtins

#print(dir(builtins))
# x = 'global x'

# def min():
#     pass

def my_min():
    pass

m = min([5,1,4,2,3])

print(m)

def test(z):
   # global x
    # y = 'local y'
    x = 'local x'
    #print(y)
    print(z)


#test('local z')
#print(y)
#print(x)
# print(z)



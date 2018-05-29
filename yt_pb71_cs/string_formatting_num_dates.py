"""
for n in range(1, 11):
    # print('The number is {}'.format(n))
    # print('The number is {:02}'.format(n))
    print('The number is {:03}'.format(n))

pi = 3.14159265

# print("The value of pi is {}".format(pi))
# print("The value of pi is {:.2f}".format(pi))
print("The value of pi is {:.3f}".format(pi))


# print('1 MB is equal to {}'.format(1000**2))

print('1 MB is equal to {:,}'.format(1000**2))

print('1 MB is equal to {:,.2f}'.format(1000**2))
"""

import datetime

current_datetime = datetime.datetime(2018, 5, 26, 8, 46, 37)

print('Current date time is {}'.format(current_datetime))

print('Current date time is {:%B %d %Y}'.format(current_datetime))

print('{0:%B %d %Y} fell on a {0:%A} on the {0:%j}th day of the year {0:%Y}'.format(current_datetime))


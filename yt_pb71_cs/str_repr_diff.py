
# The goal of __repr__ is to be unambiguous
# The goal of __str__ is to be readable
# a = [1, 2, 3, 4]
# b = 'sample string'
#
# print(str(a))
# print(repr(a))
#
# print(str(b))
# print(repr(b))

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print('str(a): {}'.format(str(a)))
print('repr(a): {}'.format(repr(a)))
print()
print('str(b): {}'.format(str(b)))
print('repr(b): {}'.format(repr(b)))

print()

c = 3+2
d = str(c)
print('str(c): {}'.format(str(c)))
print('repr(c): {}'.format(repr(c)))
print()
print('str(d): {}'.format(str(d)))
print('repr(d): {}'.format(repr(d)))

import os

my_file = '/tmp/test.txt'

# Race Condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f: # access might change by the time we come here
                            # and then there would be no way of knowing that we couldn't
                            # access file coz we though it was accessible after crossing  the if condition
        print(f.read())
else:
    print("File can't be accessed")

# No Race-Condition
try:
    f = open(my_file)
except IOError as e:
    print("FIle can't accessed")
else:
    with f:
        print(f.read())


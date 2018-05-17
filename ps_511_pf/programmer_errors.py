import sys

def convert(s):
    #Convert to an integer
    x = -1
    try:
        return int(s)
        print("Conversion succeeded! x=", x)
    except (ValueError, TypeError) as e:
        #pass
        print("Conversion error: {}".format(str(e), file=sys.stderr))
        return -1


print(convert(33))

print(convert("33"))

print(convert("dog"))

print(convert([43]))

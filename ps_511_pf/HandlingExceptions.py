def convert(s):
    #Convert to an integer
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x=", x)
    except (ValueError, TypeError):
        print("Conversion failed")
        x = -1
    return x


print(convert(33))

print(convert("33"))

print(convert("dog"))

print(convert([43]))

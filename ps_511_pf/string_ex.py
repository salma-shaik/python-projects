import math

print(len("England"))

print("New" "Found" "Land")

s = "New"
s += "Found"

print(s)

s += "Land"

print(s)

colors = ';'.join(['Hello', 'How', 'are', 'you'])
print(colors)

print(colors.split())

print(colors.split(';'))

colors1 = ''.join(['Hello', 'How', 'are', 'you'])
print(colors1)

colors2 = ' '.join(['Hello', 'How', 'are', 'you'])
print(colors2)

print("unforgetable".partition("forget"))

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure, separator, arrival)

origin, _, destination = "Seattle-Boston".partition('-')
print("No separator", origin, _, destination)

print("Her name is {0}, and age is {1}".format("Anna",34))

print("Her name is {name}, and age is {age}".format(age=34, name="Anna"))

print("Her name is {}, and age is {}".format("Anna",34))

pos=(65.2, 23.1, 53.6)

print("Galactic position = {pos[0]}, {pos[1]}, {pos[2]}".format(pos=pos))

print("From math module: pi={m.pi}, e={m.e}".format(m=math))

print("From math module: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

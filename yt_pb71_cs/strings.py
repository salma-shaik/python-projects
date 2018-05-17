greeting = 'Hello'

name = 'John'

message = greeting + ', ' + name + '. Welcome!'

print(message)

message1 = '{}, {}. Welcome!'.format(greeting, name)

print(message1)

message2 = f'{greeting}, {name.upper()}. Welcome!'

print(message2)

print(dir(str))

print(help(str))

print(help(str.lower))


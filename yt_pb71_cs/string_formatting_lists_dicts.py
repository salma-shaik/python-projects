person = {'name': 'Jenny', 'age': 23, 'job': 'Accountant'}

print('Hello my name is {} and I am {} years old'.format(person['name'], person['age']))

print('Hello my name is {0} and I am {1} years old. I work as an {2}. I have a twin sister who '
      'is also {1} years old.'.format(person['name'], person['age'], person['job']))


tag = 'h1'
text = 'This is a headline'

print('<{0}>{1}</{0}>'.format(tag, text))

print('Hello my name is {0[name]} and I am {1[age]} years old'.format(person, person))

print('Hello my name is {0[name]} and I am {0[age]} years old'.format(person))

person_info_list = ['Jenny', 23]

print('Hello my name is {0[0]} and I am {0[1]} years old'.format(person_info_list))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


pers1 = Person('Jack', 34)

print('Hello my name is {0.name} and I am {0.age} years old.'.format(pers1))

print('Hello my name is {name} and I am {age} years old'.format(name='Andy', age=32))

person = {'name': 'Jenny', 'age': 23, 'job': 'Accountant'}

print('Hello my name is {name} and I am {age} years old. I work as an {job}. I have a twin sister who '
      'is also {age} years old.'.format(**person))




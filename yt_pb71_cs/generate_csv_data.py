''' Create basic random data '''
import random

first_names = ['Amy', 'Nina', 'Clay', 'Alex', 'Justin', 'Tom', 'Brad', 'Travis', 'Mark', 'Lisa', 'Jamie']
last_names = ['Jensen', 'Archer', 'Davis', 'Stuart', 'Porter', 'Foley', 'Jones', 'Walsh', 'Doe']

with open('persons_info.csv', 'w') as pf:
    for num in range(100):
        first = random.choice(first_names)
        last = random.choice(last_names)

        email = first.lower() + last.lower() + '@fakemail.com'

        person = f'{first},{last},{email}\n'
        # print(f'{first},{last},{email}')
        pf.write(person)
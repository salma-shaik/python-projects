''' Create basic random data '''
import random

first_names = ['Amy', 'Nina', 'Clay', 'Alex', 'Justin', 'Tom', 'Brad', 'Travis', 'Mark', 'Lisa', 'Jamie']
last_names = ['Jensen', 'Archer', 'Davis', 'Stuart', 'Porter', 'Foley', 'Jones', 'Walsh', 'Doe']
street_names = ['Windy Rd', 'Bullhead', 'Bancroft', 'Hudson', 'Burlington', 'Secor', 'Dorr', 'Douglas', 'Berdan']
fake_cities = ['Westeros', 'Toledo', 'Troy', 'Dayton', 'Findley', 'Miami', 'Chicago', 'Apex', 'Raleigh']
states = ['AL', 'OH', 'MI', 'NE', 'CA', 'IL', 'IA', 'NC', 'SC', 'GA', 'TN', 'KY', 'FL', 'CO', 'WA']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100,999)
    street = random.choice(street_names)

    city = random.choice(fake_cities)
    state = random.choice(states)

    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@fakemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')

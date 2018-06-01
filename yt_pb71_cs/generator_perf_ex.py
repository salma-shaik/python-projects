import memory_profiler
import random
import time

names = ['Amy', 'Nina', 'Clay', 'Alex', 'Justin', 'Trevor']
majors = ['Math', 'History', 'Art', 'Engineering', 'Chemistry', 'Physics']

print('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))


# generating a list of people
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': 1,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result


# generating a list of people using generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': 1,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


# clocking time with people_list
# t1 = time.clock()
#people = people_list(1000000)
#t2 = time.clock()


# clocking time with generator
t1 = time.clock()
people = people_generator(1000000)
# less performant again if we convert to list
people = list(people_generator(1000000))
t2 = time.clock()

# Printing memory and time stats
print ('Memory (After): {}Mb'.format(memory_profiler.memory_usage()))
print('Took {} seconds'.format(t2-t1))

courses = ['history', 'maths', 'physics', 'compsci']

# print(courses)
#
# print(courses[0])
#
# print(courses[3])
#
# print(courses[-1])
#
# print(courses[-4])
#
# print(courses[0:2])
#
# #print(courses[2:4])
# print(courses[2:])

"""
print(courses[-4:-2])

courses.append('art')

print(courses)

courses.insert(0,'language')

print(courses)

courses2 = ['education', 'psychology']

courses.insert(0, courses2)

print(courses)

print(courses[0])

del courses[0]

print(courses)

courses.extend(courses2)

print(courses)

courses.remove('art')

print(courses)

print(courses.pop())

#Sort lists
courses.reverse()
print(courses)

courses.sort()
print(courses)

num = [8,45,89,34,0,54]

# num.sort()
#
# print(num)
#
# num.sort(reverse=True)
# print(num)


sorted_courses = sorted(courses)

print(sorted_courses)

print(min(num))

print(max(num))
print(sum(num))

print(courses.index('compsci'))
#print(courses.index('art'))
print('art' in courses)
print('maths' in courses)

for item in courses:
    print(item)


for index,course in enumerate(courses):
    print(index,course)

print('\n')

for index,course in enumerate(courses, start=1):
    print(index,course)

course_str = ', '.join(courses)

print(course_str)

course_from_str = course_str.split(', ')

print(course_from_str)


# Mutable Example

list1 = ['history', 'maths', 'physics', 'compsci']
list2 = list1

print(list1)
print(list2)

list2[1] = 'art'

print(list1)
print(list2)



# Immutable

tup1 = ('history', 'maths', 'physics', 'compsci')
tup2 = tup1

print(tup1)
print(tup2)



tup1[1] = 'art'

print(tup1)
print(tup2)
"""

# Set
courses_set = {'history', 'maths', 'physics', 'compsci'}
art_courses_set = {'history', 'art', 'physics', 'design'}

print(courses_set)

courses_set1 = {'history', 'maths', 'physics', 'compsci', 'maths'}
print(courses_set1)

print('maths' in courses_set)

print(courses_set.intersection(art_courses_set))

print(courses_set.difference(art_courses_set))

print(courses_set.union(art_courses_set))


# Empty List
empty_list = []
empty_list = list()

# Empty Tuple
empty_tup = ()
empty_tup = tuple()

# Empty set
# empty_set = {} - creates empty dict!
empty_set = set()
print(empty_list, empty_set, empty_tup)
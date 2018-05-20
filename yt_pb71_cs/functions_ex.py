def hello_func(greeting, name = 'You'):
    #print('Hello Function!')
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', name = 'Corey'))

courses = ['Math', 'Art']
info = {'name':'John', 'age':22}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


#student_info(courses, info)
student_info(*courses, **info)


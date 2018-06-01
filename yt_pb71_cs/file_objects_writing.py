with open('file_object_writetest.txt', 'w') as f:
    f.write('test \n')
    f.seek(0)
    # f.write('test \n')
    f.write('r')

with open('file_object_writetest.txt', 'a') as f:
    f.write('test2')
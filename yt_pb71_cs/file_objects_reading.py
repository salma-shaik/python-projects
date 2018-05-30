""" 1. If we open the file like this, then its important to always close the file
otherwise we can end up with leaks that cause us to run over the maximum allowable
file descriptors in the system and applications can throw errors.
"""

'''
test_file_ref = open('file_object_test.txt', 'r')
print('File Name: ', test_file_ref.name)
print('File Mode: ', test_file_ref.mode)
test_file_ref.close()
'''

"""
Due to 1), context manager is a better option
"""
with open('file_object_test.txt', 'r') as test_file_ref:
    """
    print('File Name: ', test_file_ref.name)
    print('File Mode: ', test_file_ref.mode)
    # test_file_ref.contents = test_file_ref.read()
    # print("All contents read: \n", test_file_ref.contents)
    print('One line at a time: ', test_file_ref.readline(), end='')
    print('One line at a time: ', test_file_ref.readline(), end='')
    print('One line at a time: ', test_file_ref.readline(), end='')
    """

    """
    # Iterating through file
    for f in test_file_ref:
        print(f,end='')
    """

    """
    size_to_read = 100
    test_file_ref.contents = test_file_ref.read(size_to_read)
    # Read specific number of characters at a time
    
    while len(test_file_ref.contents)>0:
        print("Current position: ", test_file_ref.tell())
        print(test_file_ref.contents, end='')
        test_file_ref.contents = test_file_ref.read(size_to_read)
    """
    size_to_read = 10
    test_file_ref.contents = test_file_ref.read(size_to_read)
    print(test_file_ref.contents, end='')

    test_file_ref.seek(0)

    test_file_ref.contents = test_file_ref.read(size_to_read)
    print(test_file_ref.contents)

"""
print(test_file_ref.closed)
print(test_file_ref.name)

# Eventhough we can get info about file object,we can't read data from it.
# So we will have to work with the file object from within the context manager.
# print(test_file_ref.read())
"""


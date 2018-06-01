with open('file_object_test.txt', 'r') as rf:
    with open('file_object_test_copy.txt', 'w') as wf:
        for line in rf.read():
            wf.write(line)


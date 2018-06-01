try:
    f = open('test_file1.txt', 'r')
    # random_var = bad_var
except FileNotFoundError as e:
    print(e)
    # print('File not found!')
except NameError as e:
    print('Undefined variable')

else:
    print(f.read())
    f.close()

finally:
    print("Executing Finally...")

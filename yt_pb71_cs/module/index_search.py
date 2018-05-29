print("Importing index_search module ....")

test = 'Test String'

print(test)



def find_index(content, target):
    for i,value in enumerate(content):
        if value == target:
            return i


from pprint import pprint as pp

"""
id_names = [(2, 'sam'),(6, 'anna'), (4, 'joe')]

dict1 = dict(id_names)

print(dict1)

dict2 = dict(a='alpha', b='bravo', c='charlie')

print(dict2)

dict3 = dict2.copy()

print(dict3)

dict4 = dict(dict2)

print(dict4)

update_dict = dict(d = 'danny', e='epsilon')

dict2.update(update_dict)

print(dict2)

update_dict1 = dict(d='daniel', f='fairy')

dict2.update(update_dict1)

print(dict2)


for key in dict2:
    print("Key: " + key + ",Value: " + dict2[key])


for value in dict2.values():
    print(value)

for key in dict2.keys():
    print(key)

for key, value in dict2.items():
    print("{key} =====> {value}".format(key=key, value=value))


print('a' in dict2)

print('alpha' in dict2)

del dict2['c']

print(dict2)

"""

dict_list = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]}

dict_list['B'] += [6,5,4]

#print(dict_list)

dict_list['D'] = [10,11,12]

print(dict_list)
 
pp(dict_list)


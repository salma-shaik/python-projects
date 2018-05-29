nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
# Get n for each n in nums
num_list = [n for n in nums]
print(num_list)

# Get n^2 for each n in nums
# num2_list = [n**2 for n in nums]
num2_list = [n*n for n in nums]
print(num2_list)

# Get n for each n in nums if n is even
even_num_list = [n for n in nums if n % 2 == 0]
print(even_num_list)


# Get a (letter, num) pair for each letter in 'abcd' and each number in '0123'
word = 'abcd'
number = '0123'


pair_list = []
for l in word:
    for n in number:
        tup = (l, n)
        pair_list.append(tup)
print(pair_list)


# letter_num_list = [(l, n) for l in word for n in number]
letter_num_list = [(l, n) for l in 'abcd' for n in range(4)]
print(letter_num_list)



list_from_word = list(word)
list_from_num = list(number)


print(list_from_word)
print(list_from_num)

['a', 'b', 'c', 'd']
['0', '1', '2', '3']

zip_list = zip(list_from_word, list_from_num)
print(zip_list)

for item in zip_list:
    print(item)

print(list(zip(list_from_word, list_from_num)))

# Dictionary Comprehensions
dict_ln = {}
for l, n in zip(list_from_word, list_from_num):
    dict_ln[l] = n
print(dict_ln)

dict_ln_compr = {l: n for l, n in zip(list_from_word, list_from_num)}
print(dict_ln_compr)

dict1_ln_compr = {l: n for l, n in zip(list_from_word, list_from_num) if l != 'c'}
print(dict1_ln_compr)

# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
set_nums = set(nums)
print(set_nums)

set_compr = {n for n in nums}
print(set_compr)

# Generator Expressions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n*n


num_gen = gen_func(nums)

for i in num_gen:
    print (i)
'''

gen_from_exp = (n*n for n in nums)

for i in gen_from_exp:
    print(i)

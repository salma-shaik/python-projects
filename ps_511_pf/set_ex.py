"""
set1 = {3,6,234,7,7,8,9,9}

print(set1)

set2 = set([43,45,2,6,34,8,4,8,342,34,7,2])

print(set2)

for t in set2:
    print(t)

print(3 in set2)

print(0 not in set2)

set2.add(100)
set2.add(43)

print(set2)

set2.update([1, 11])

print(set2)

set2.remove(1)

#set2.remove(0)

print(set2)

set2.discard(0)

set_copy = set2.copy()

print("set_copy: ", set_copy)

set_copy1 = set(set2)

print("set_copy1: ",set_copy1)
"""

blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

print(blue_eyes.union(blond_hair))

print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

print(blue_eyes.intersection(blond_hair))

print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

print(blond_hair.difference(blue_eyes))

print(blond_hair.symmetric_difference(blue_eyes))

print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

print(smell_hcn.issubset(blond_hair))

print(ab_blood.isdisjoint(b_blood))

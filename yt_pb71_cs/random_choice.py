import random

"""
rvalue = random.random()
print((rvalue))

rvalue1 = random.uniform(1,10)
print(rvalue1)

rvalue2 = random.randint(1,6)
print(rvalue2)

list1 = ['Red', 'Yellow', 'Green', 'Blue', 'Orange']
rlist1 = random.choice(list1)
#print(rlist1)

rlist2 = random.choices(list1, k=2)
print(rlist2)

list2 = ['Red', 'Yellow', 'Green']
rlist3 = random.choices(list2, weights=[20,7,2], k=10)
print(rlist3)
"""

deck1 = list(range(1,53))
print(deck1)

random.shuffle(deck1)
print(deck1)

# sample - grabs unique from the sequence
deck_hand = random.sample(deck1, k=5)
print(deck_hand)
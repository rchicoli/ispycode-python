
import itertools, random

deck = list(itertools.product(range(1,14),['Spades','Hearts','Diamonds','Clubs']))

random.shuffle(deck)

print("Your cards:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])



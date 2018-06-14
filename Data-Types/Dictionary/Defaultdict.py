
from collections import defaultdict

icecream = defaultdict(lambda: 'Vanilla')

icecream['Tom'] = 'Chocolate'
icecream['Bob'] = 'Strawberry'

print icecream['Tom']
print icecream['Bob']
print icecream['John']




from collections import Counter

str = "the cat in the hat"

c = Counter()

for char in str:
  c.update(char)

for letter, count in c.most_common():
    print('%s: %d' % (letter, count))



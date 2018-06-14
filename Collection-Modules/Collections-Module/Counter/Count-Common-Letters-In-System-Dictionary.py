
from collections import Counter

c = Counter()

with open('/usr/share/dict/words', 'rt') as f:
  for line in f:
    c.update(line.rstrip().lower())

print("Most common:")
for letter, count in c.most_common(10):
    print('%s: %4d' % (letter, count))



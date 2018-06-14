
from collections import Counter

# list of colors
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']

# create a counter
counter = Counter()

# count colors
for word in colors:
  counter[word] += 1

# print results
print (counter)



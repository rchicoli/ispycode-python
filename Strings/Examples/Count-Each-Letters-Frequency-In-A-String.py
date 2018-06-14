
import re

str = 'the quick brown fox jumps over the lazy dog'
str = str.lower()
print(str)

str = re.sub("[^A-Za-z]", "", str)
print(str)

dict = &#123;&#125;
for n in str:
  keys = dict.keys()
  if n in keys:
    dict[n] += 1
  else:
    dict[n] = 1

for key, value in dict.items():
   print(key,value)



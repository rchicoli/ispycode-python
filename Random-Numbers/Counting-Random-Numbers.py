
import random
numbers = &#123;&#125;

for x in range(100000):
  i = random.randrange(10,20)
  if i not in numbers:
    numbers[i] = 1
  else:
    numbers[i] = numbers.get(i) + 1

for key, value in numbers.items():
   print(key,value)



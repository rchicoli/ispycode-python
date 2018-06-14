
import itertools

for i in itertools.islice('ABCDEFG', 2):
  print(i)

print("-----")

for i in itertools.islice('ABCDEFG', 2, 4):
  print(i)

print("-----")

for i in itertools.islice('ABCDEFG', 2, None):
  print(i)

print("-----")

for i in itertools.islice('ABCDEFG', 0, None, 2):
  print(i)



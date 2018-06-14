
d1 = &#123;'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 1&#125;
d2 = &#123;&#125;

for key,value in d1.items():
  if value not in d2.values():
    d2[key] = value

print(d1)
print(d2)



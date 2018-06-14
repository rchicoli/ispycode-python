
# create an empty dictionary
d = {'a':1,'b':2,'c':3,'d':4}
print(d)

# get value of a (use 5 if not set)
a = d.setdefault('a', 5)
print(a)

# get value of e (use 5 if not set)
e = d.setdefault('e', 5)
print(e)

print(d)



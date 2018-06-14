
def gcd(a, b):
  if b==0:
    return a
  return gcd(b, a%b)

results = gcd(10,5)
print(results)

results = gcd(999,666)
print(results)



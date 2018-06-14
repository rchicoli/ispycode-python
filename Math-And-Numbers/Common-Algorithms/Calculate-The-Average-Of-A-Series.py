def average(seq):
  return float(sum(seq)) / len(seq)

list = (1,2,3,4,5,6,7,8,9)
results = average(list)
print(results)


def average(seq, total=0.0):
  num = 0
  for item in seq:
    total += item
    num += 1
  return total / num


list = (1,2,3,4,5,6,7,8,9)
results = average(list)
print(results)



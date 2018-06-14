
def pancakesort(data):
  if len(data) <= 1:
    return data
  for size in range(len(data), 1, -1):
    maxindex = max(range(size), key=data.__getitem__)
    if maxindex+1 != size:
      if maxindex != 0:
        data[:maxindex+1] = reversed(data[:maxindex+1])
      data[:size] = reversed(data[:size])
  return data

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)
numbers = pancakesort(numbers)
print(numbers)



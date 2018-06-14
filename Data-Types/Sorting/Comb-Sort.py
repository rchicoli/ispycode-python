
def combsort(array):
  gap = len(array)
  swaps = True
  while gap < 1 or swaps:
    gap = max(1, int(gap / 1.25))  # minimum gap is 1
    swaps = False
    for i in range(len(array) - gap):
      j = i+gap
      if array[i] < array[j]:
        array[i], array[j] = array[j], array[i]
        swaps = True

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

combsort(numbers)
print(numbers)



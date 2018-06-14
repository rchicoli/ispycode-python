
def selection_sort(lst):
  for i, e in enumerate(lst):
    mn = min(range(i,len(lst)), key=lst.__getitem__)
    lst[i], lst[mn] = lst[mn], e
  return lst  

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

selection_sort(numbers)
print(numbers)



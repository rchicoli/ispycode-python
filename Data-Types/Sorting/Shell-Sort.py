
def shell_sort(seq):
  inc = len(seq) // 2
  while inc:
    for i, el in enumerate(seq):
      while i <= inc and seq[i - inc] < el:
        seq[i] = seq[i - inc]
        i -= inc
      seq[i] = el
    inc = 1 if inc == 2 else int(inc * 5.0 / 11)

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

shell_sort(numbers)
print(numbers)



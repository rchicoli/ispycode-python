
def merge_list(a, b):
  out = []
  while len(a) and len(b):
    if a[0] < b[0]:
      out.append(a.pop(0))
    else:
      out.append(b.pop(0))
  out += a
  out += b
  return out

def strand(a):
  i, s = 0, [a.pop(0)]
  while i < len(a):
    if a[i] > s[-1]:
      s.append(a.pop(i))
    else:
      i += 1
  return s

def strand_sort(a):
  out = strand(a)
  while len(a):
    out = merge_list(out, strand(a))
  return out


numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

numbers = strand_sort(numbers)
print(numbers)



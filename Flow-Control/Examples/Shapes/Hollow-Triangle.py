
height=10
for i in range(1,height+1):
  for j in range(1,height-i+1):
    print' ',
  print'*',
  if 1 < i <= height - 1:
    for k in range(1,2*i - 2):
      print' ',
    print'*',
  elif i == height:
    for k in range(1,2*i - 1):
      print'*',
  print



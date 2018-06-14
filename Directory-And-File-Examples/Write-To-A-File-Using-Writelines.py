
colors = ['red', 'orange', 'yellow', 'blue']
f = open('colors.txt', 'w')
for color in colors:
  f.writelines(color)
  f.writelines('\n')
f.close()



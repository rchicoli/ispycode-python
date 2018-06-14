
import fileinput

for line in fileinput.input('example.py'):
  print(fileinput.lineno())
  fileinput.close()



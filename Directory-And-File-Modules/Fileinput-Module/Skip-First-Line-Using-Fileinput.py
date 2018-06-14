
import fileinput

for line in fileinput.input('file.txt'):
  if not fileinput.isfirstline():
    print(line.strip('\n'))



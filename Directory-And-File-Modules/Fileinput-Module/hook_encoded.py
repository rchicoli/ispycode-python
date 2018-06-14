
import fileinput

for line in fileinput.input('file.txt', openhook=fileinput.hook_encoded("iso-8859-1")):
  print(line.strip('\n'))



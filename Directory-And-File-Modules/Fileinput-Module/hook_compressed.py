
import fileinput

for line in fileinput.input('file.txt.gz', openhook=fileinput.hook_compressed):
  print(line.strip('\n'))



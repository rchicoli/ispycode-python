
import fileinput
import sys

for line in fileinput.input(sys.argv[1:]):
  print(fileinput.filename())
  fileinput.nextfile()



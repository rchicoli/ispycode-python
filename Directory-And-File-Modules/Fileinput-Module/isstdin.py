
import fileinput
import sys

for line in fileinput.input(sys.stdin.seek(0)):
   print(fileinput.isstdin())
   print(line.strip('\n'))



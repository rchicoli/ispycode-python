
import enum

class Number(enum.IntEnum):
  one = 1
  two = 2
  three = 3
  four = 4

var1 = Number.one

if(var1 == 1):
  print("var1 is equal to 1")



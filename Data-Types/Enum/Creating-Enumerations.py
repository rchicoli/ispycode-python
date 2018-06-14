
from enum import Enum

class Day(Enum):
  sunday = 1
  monday = 2
  tuesday = 3
  wednesday = 4
  thursday =5
  friday = 6
  saturday = 7

print(Day.monday)
print(repr(Day.monday))



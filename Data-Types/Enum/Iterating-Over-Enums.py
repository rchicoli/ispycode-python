
from enum import Enum

class Day(Enum):
  sunday = 1
  monday = 2
  tuesday = 3
  wednesday = 4
  thursday =5
  friday = 6
  saturday = 7

for day in Day:
  print('{:9}: {}'.format(day.name, day.value))



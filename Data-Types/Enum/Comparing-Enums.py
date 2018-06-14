
from enum import Enum

class Day(Enum):
  sunday = 1
  monday = 2
  tuesday = 3
  wednesday = 4
  thursday =5
  friday = 6
  saturday = 7


day1 = Day.monday
day2 = Day.tuesday
day3 = Day.monday

print(day1 == day2)
print(day1 == day3)



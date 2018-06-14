
from enum import Enum

class Status(Enum):
  pending = 1
  active = 2
  inactive = 3
  deleted = 4
  recovering = 1


status1 = Status.pending
status2 = Status.recovering

print(status1 == status2)



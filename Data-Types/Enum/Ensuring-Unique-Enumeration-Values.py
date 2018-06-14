
from enum import Enum

@enum.unique
class Status(Enum):
  pending = 1
  active = 2
  inactive = 3
  deleted = 4
  recovering = 1



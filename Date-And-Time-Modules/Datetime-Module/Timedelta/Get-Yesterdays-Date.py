
from datetime import timedelta
from datetime import date

today = date.today()
print(today)

yesterday = date.today() + timedelta(-1)
print(yesterday)



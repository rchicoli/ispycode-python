
import datetime

today = datetime.date.today()
for x in range(0, 10):
  delta = today + datetime.timedelta(days=x)
  print delta



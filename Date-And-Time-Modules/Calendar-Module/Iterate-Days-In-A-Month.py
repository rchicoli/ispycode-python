
import calendar

c = calendar.Calendar()
for date in c.itermonthdates(2016, 7):
  print(date)



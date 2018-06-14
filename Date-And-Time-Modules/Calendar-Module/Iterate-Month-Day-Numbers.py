
import calendar

c = calendar.Calendar()
for day in c.itermonthdays(2016, 7):
  if(day != 0):
    print(day)



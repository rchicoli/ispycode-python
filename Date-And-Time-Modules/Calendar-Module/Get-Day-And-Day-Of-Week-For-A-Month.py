
import calendar

c = calendar.Calendar()
for tuple in c.itermonthdays2(2016, 7):
  day, weekday = tuple
  if(day != 0):
    print("%s : %s" % (day,calendar.day_name[weekday]))



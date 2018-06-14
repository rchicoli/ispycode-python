
import calendar

c = calendar.Calendar()
for tuple in c.monthdays2calendar(2016, 7):
  for week in tuple:
    day, weekday = week
    if(day != 0):
      print("%s : %s" % (day,calendar.day_name[weekday]))



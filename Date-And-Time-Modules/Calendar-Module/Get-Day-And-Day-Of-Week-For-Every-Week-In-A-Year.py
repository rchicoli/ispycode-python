
import calendar

c = calendar.Calendar()
tuples = c.yeardays2calendar(2016)
for year in tuples:
  for month in year:
    for week in month:
      for day,weekday in week:
        if(day != 0):
          print("%s : %s" % (day,calendar.day_name[weekday]))



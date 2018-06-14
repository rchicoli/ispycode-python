
import calendar

c = calendar.Calendar()
list=c.yeardatescalendar(2016)
for year in list:
  for month in year:
    for week in month:
      for day in week:
        print("%s/%s/%s" % (day.month, day.day, day.year))



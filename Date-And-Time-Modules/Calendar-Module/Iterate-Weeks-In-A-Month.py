
import calendar

c = calendar.Calendar()
for week in c.monthdatescalendar(2016, 7):
  for day in week:

    print("%s/%s/%s" % (day.day,day.month,day.year))



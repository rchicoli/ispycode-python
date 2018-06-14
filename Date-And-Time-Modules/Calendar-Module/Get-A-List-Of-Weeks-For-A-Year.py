
import calendar  

c = calendar.Calendar()
months = c.yeardayscalendar(2016)
for month in months:
  for weeks in month:
    for week in weeks:
      print(week)



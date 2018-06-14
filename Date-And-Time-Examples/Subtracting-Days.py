
import datetime

now = datetime.date.today()
delta = now - datetime.timedelta(days=30)

print('Today      : %s ' % (now) )
print('30 days ago: %s ' % (delta) )



import datetime
import pytz

time1 = datetime.time(9, 16, 30, 100000)
print(time1)
print(time1.hour)

datetime1 = datetime.datetime(2010, 12, 14, 12, 56, 34, 100000)
print(datetime1)
print(datetime1.date())
print(datetime1.time())
print(datetime1.year)

datedelta1 = datetime.timedelta(days=7)
print('Week ahead from datetime1:', datetime1+datedelta1)

timedelta1 = datetime.timedelta(hours=10)
print('Time 10 hours from now:', datetime1+timedelta1)



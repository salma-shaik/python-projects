import datetime
import pytz

"""
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
"""

# Timezone
# create time zone aware datetime using utc
datetime1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(datetime1)

datetime1_now = datetime.datetime.now(tz=pytz.UTC)

'''
print('datetime1_now in UTC: ', datetime1_now)

dt_mtn = datetime1_now.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)
'''

# strftime - converts datetime to a string
date_str = datetime1_now.strftime('%B %d, %Y')
print('Formatted date time: ', date_str)

# strptime - converts string to a datetime
print('Date time from date string: ', datetime.datetime.strptime(date_str, '%B %d, %Y'))

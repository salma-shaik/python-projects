import datetime

datetime1 = datetime.datetime(2019, 3, 23)
print(datetime1)

date1 = datetime.date(2019, 3, 23)
print(date1)

today = datetime.date.today()
print(today)
print(today.weekday())
print(today.isoweekday())

# Time deltas - diff between 2 dates or times
timedelta1 = datetime.timedelta(7)
print("Date 7 days from now: ", today+timedelta1)
print("Date 7 days ago: ", today-timedelta1)


# date2 = date1 +/- timedelta
# timedelta = date1 +/- date2
bday = datetime.date(2018, 11, 16)
till_bday = bday - today
print("Days left for my birthday:", till_bday.days)
# print("Seconds left for my birthday:", int(till_bday.total_seconds()))








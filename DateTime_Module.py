import datetime

t = datetime.time(14, 33, 44)
print (t)
print t.hour, t.minute, t.second, t.microsecond

print datetime.time.min
print datetime.time.max
print datetime.time.resolution

today = datetime.date.today()
print (today)
print (today.timetuple())
print (today.day)
print (today.resolution)
past_date = today.replace(2006)
print (past_date)
no_of_days = today - past_date
print (no_of_days)

from datetime import datetime
from datetime import timedelta

def TestDate (date):
	if (date.month == 3 and date.day >= 21):
		return True
	if (date.month == 4 and date.day <= 7):
		return True
	return False

def GetLastSunday (date):
	lastsundaydelta = timedelta (days=((date+timedelta (days=1)).weekday()))
	return date-lastsundaydelta

n = 0
mooncycleindays = timedelta (days=29.530587981)
today = datetime(2017,3,12,6,34,0)
foundationdate = datetime(1871,10,8,0,0,0)
testdate = today
while testdate > foundationdate:
	testdate = testdate-mooncycleindays
	print testdate
	if (TestDate (testdate)):
		if (GetLastSunday (testdate).month == 3):
			print "---"
			print testdate
			print (GetLastSunday (testdate))
			n=n+1
print n

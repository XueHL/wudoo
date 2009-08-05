inputName = "calendar.txt"

import datetime
DAYNORM = 8.5
DAYNORM = datetime.timedelta(seconds = int(60.0 * 60.0 * DAYNORM))

WEEKNORM = DAYNORM * 4
print WEEKNORM

### ### ### ### ### ### ### ### ### ###

import sys, os
sys.path.append(os.path.join(__file__, "..", "..", ".."))
from wudoo.timeutils.HRBOParse import *

### ### ### ### ### ### ### ### ### ###

buf = open(inputName, "r").read()
weekList = parseMonth(buf)
lastWeek = weekList[len(weekList) - 1]
for dayDist in lastWeek.dayDists:
	print dayDist

weeksum = None
remaindDays = 5
for dayDist in lastWeek.dayDists:
	if dayDist is None:
		continue
	remaindDays -= 1
	cd = dayDist.dayEndTime - dayDist.dayBegTime
	if weeksum is None:
		weeksum = cd
	else:
		weeksum = weeksum + cd

hours = weeksum.days * 24.0 + float(weeksum.seconds) / (60.0 * 60.0)
hoursint = int(hours)
hours -= hoursint
minutes = hours * 60.0
minutesint = int(minutes)
minutes -= minutesint
seconds = minutes * 60.0
secondsint = int(seconds)
print str(hoursint) + " H " + str(minutesint) + " M " + str(secondsint) + " S"

print "remaind", WEEKNORM - weeksum

if remaindDays > 0:
	print "remaind per day", (WEEKNORM - weeksum) / remaindDays
inputName = "calendar.txt"

import datetime
DAYNORM = 8.5
DAYNORM = datetime.timedelta(seconds = int(60.0 * 60.0 * DAYNORM))

WEEKNORM = DAYNORM * 4
#print WEEKNORM

### ### ### ### ### ### ### ### ### ###

import sys, os
sys.path.append(os.path.join(__file__, "..", "..", ".."))
from wudoo.timeutils.HRBOParse import *

### ### ### ### ### ### ### ### ### ###

buf = open(inputName, "r").read()
weekList = parseMonth(buf)
lastWeek = weekList[len(weekList) - 1]
for dayDist in lastWeek.workDays:
	print dayDist

weeksum = datetime.datetime.now() - datetime.datetime.now()
remaindDays = 5
for workDay in lastWeek.workDays:
	if workDay is None or workDay.isEmpty():
		continue
	remaindDays -= 1
	cd = workDay.getTotalWorkTime()
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

rmnd = WEEKNORM - weeksum
rmndh = rmnd.seconds / 3600
rmndm = rmnd.seconds / 60 - rmndh * 60
rmnds = rmnd.seconds - rmndm * 60 - rmndh * 3600
rmndh += rmnd.days * 24.0
print "remaind ", rmndh, "H ", rmndm, "M ", rmnds, "S"

if remaindDays > 0:
	print "remaind per day", (WEEKNORM - weeksum) / remaindDays, " ( ", (WEEKNORM - weeksum) / (remaindDays + 1)," )"
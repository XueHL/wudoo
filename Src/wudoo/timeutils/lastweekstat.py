inputName = "calendar.txt"

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
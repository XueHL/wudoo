inputName = "calendar.txt"

### ### ### ### ### ### ### ### ### ###

import sys, os
sys.path.append(os.path.join(__file__, "..", "..", ".."))
from wudoo.timeutils.HRBOParse import *

### ### ### ### ### ### ### ### ### ###

buf = open(inputName, "r").read()
weekDists = parseWeekDists(buf)
lastWeek = weekDists[len(weekDists) - 1]
print lastWeek.dayDists
VALLEY = "valley-o"
BOG = "bog"
PRI = "O-ro the rattlin' bog, the bog down in the " + VALLEY
ITEMS_LIST = "tree;limb;branch;nest;egg;bird;feather;flea".split(";")
IN_WORDS = "bog;nest;egg"

FIRST_BEG = "And in"
USUAL_BEG = "Now on"
BEG_TEMPLATE = " that %prev% there was a %cur%, a rare %cur%, a rattlin' %cur%"

FIRST_MAIN_BEG = "With "
USUAL_MAIN_BEG = "and "
MAIN_TEMPLATE = "the %cur_l% %on<>in% the %prev_l%"

END = "And the bog down in the valley-o."

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

from wudoo.textproc.Front import *

tproc = getTextProc("Rattling-bog", __file__)

tproc.setBookName("Rattling bog song")

tproc.addHeader(level = 0, headerText = "Rattling bog")

for i in xrange(2):
	tproc.newParagraph()
	tproc.write(PRI)

prevItem = BOG
curBeg = FIRST_BEG
userItems = [BOG]
for item in ITEMS_LIST:
	tproc.newParagraph()
	tproc.write(curBeg)
	curBeg = USUAL_BEG
	begLine = BEG_TEMPLATE.replace("%prev%", prevItem).replace("%cur%", item)
	tproc.write(begLine)
	userItems = [item] + userItems

	tproc.newParagraph()
	mcurBeg = FIRST_MAIN_BEG
	n = len(userItems)
	for i in xrange(n-1):
		tproc.write(mcurBeg)
		mcurBeg = USUAL_MAIN_BEG
		cur_l = userItems[i]
		prev_l = userItems[i+1]
		on_in = "on"
		if IN_WORDS.find(prev_l) > -1:
			on_in = "in"
		mainLinePart = MAIN_TEMPLATE.replace("%cur_l%", cur_l).replace("%prev_l%", prev_l).replace("%on<>in%", on_in)
		
		tproc.write(mainLinePart)
	tproc.write(".")		
	tproc.newParagraph()
	tproc.write(END)
	
tproc.stop()

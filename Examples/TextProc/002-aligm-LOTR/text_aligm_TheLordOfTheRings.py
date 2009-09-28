from wudoo.textproc.Front import *

tproc = getTextProc("the-lord-of-the-lings--wikipedia-article", __file__)
saveStrat = tproc.getOnStopStrategy()
saveStrat.setFileName("Wiki-TLOTR")
saveStrat.getSaverFactory().setPageWidth(100)

runScript("..", "000-trivial-text-aligm", "TheLordOfTheRings.py")

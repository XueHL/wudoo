from wudoo.textproc.save.ISaverFactory import ISaverFactory
from wudoo.textproc.save.text.TextSaver import TextSaver
from wudoo.textproc.save.ISaverFactory import ISaverFactory

class TextSaverFactory(ISaverFactory):
	def __init__(self):
		self.__pgWidth = -1

	def newSaver(self):
		textSaver = TextSaver()
		textSaver.setPageWidth(self.__pgWidth)
		return textSaver

	def setPageWidth(self, pgWidth):
		self.__pgWidth = pgWidth
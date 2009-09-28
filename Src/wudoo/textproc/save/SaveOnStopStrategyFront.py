from wudoo.textproc.save.IOnStopStrategy import IOnStopStrategy
from wudoo.textproc.save.text.TextSaverFactory import TextSaverFactory

class SaveOnStopStrategyFront(IOnStopStrategy):
	def __init__(self, fileName = "DEFAULT_FILE_NAME"):
		self.__fileName = fileName
		self.__saverFactory = TextSaverFactory()

	def onStop(self, document):
		fileName = self.__fileName
		saver = self.__saverFactory.newSaver()
		fileName += "." + saver.getExtension()
		file = open(fileName, "w")
		saver.setFile(file)
		document.visit(saver)
		file.close()

	def setFileName(self, fileName):
		self.__fileName = fileName

	def getSaverFactory(self):
		return self.__saverFactory
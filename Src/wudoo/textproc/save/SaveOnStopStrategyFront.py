from wudoo.textproc.save.IOnStopStrategy import IOnStopStrategy
from wudoo.textproc.save.text.TextSaver import TextSaver

class SaveOnStopStrategyFront(IOnStopStrategy):
	def onStop(self, document):
		fileName = self.getFileName(document)
		saver = self.getSaver(document)
		fileName += "." + saver.getExtension()
		file = open(fileName, "w")
		saver.setFile(file)
		document.visit(saver)
		file.close()

	def getFileName(self, document):
		return "DEFAULT_FILE_NAME"

	def getSaver(self, document):
		return TextSaver()
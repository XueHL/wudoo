from wudoo.textproc.processing.tools.ITool import ITool

class ParagraphTool(ITool):
	def __init__(self, textProcessor):
		self.__textProcessor = textProcessor
		self.__buffer = ""

	def dispose(self):
		toolsList = self.__textProcessor.getToolsList()
		n = len(toolsList)
		if  toolsList[n - 1] is not self:
			raise InvalidUssage()

	def appendText(self, text):
		self.__buffer += " " + text

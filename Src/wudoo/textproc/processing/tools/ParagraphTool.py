from wudoo.textproc.processing.tools.ITool import ITool
from wudoo.textproc.document.elements.Paragraph import Paragraph
from wudoo.textproc.document.elements.TextBit import TextBit

class ParagraphTool(ITool):
	def __init__(self, textProcessor):
		self.__textProcessor = textProcessor
		self.__buffer = ""

	def dispose(self):
		toolsList = self.__textProcessor.getToolsList()
		n = len(toolsList)
		if  toolsList[n - 1] is not self:
			raise InvalidUssage()
		paragraph = Paragraph()
		paragraph.appendElement(TextBit(ParagraphTool.reduceBuffer(self.__buffer)))
		self.__textProcessor.getDocumtnt().appendElement(paragraph)

	def appendText(self, text):
		self.__buffer += " " + text

	def __reduceBuffer(buf):
		buf = buf.replace("\n", " ").split(" ")
		result = ""
		for word in buf:
			if len(word) == 0:
				continue
			if len(result) > 0:
				result += " "
			result += word
		return result
	reduceBuffer = staticmethod(__reduceBuffer)

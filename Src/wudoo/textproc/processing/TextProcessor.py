from wudoo.textproc.processing.ITextProcessor import ITextProcessor
from wudoo.textproc.processing.DefaultToolsOperationStraegy import DefaultToolsOperationStraegy
from wudoo.textproc.processing.tools.ParagraphTool import ParagraphTool
from wudoo.textproc.processing.tools.ButtomTool import ButtomTool
from wudoo.textproc.save.SaveOnStopStrategyFront import SaveOnStopStrategyFront
from wudoo.textproc.document.elements.Document import Document
from wudoo.textproc.document.elements.Header import Header

class TextProcessor(ITextProcessor):
	def __init__(self, docName, scriptFile):
		self.__docName = docName
		self.__scriptFile = scriptFile
		self.__document = Document()
		self.__tools = [ButtomTool()]
		self.__toolsOperationStraegy = DefaultToolsOperationStraegy()
		self.__onStopStrategy = SaveOnStopStrategyFront()

	def setBookName(self, name):
		self.__document.getBookName().set(name)

	def addHeader(self, level, headerText):
		header = Header(level = level, headerText = headerText)
		self.__document.appendElement(header)

	def newParagraph(self):
		self.__toolsOperationStraegy.appendTool(self.__tools, ParagraphTool(self))

	def write(self, text):
		n = len(self.__tools)
		tool = self.__tools[n - 1]
		tool.appendText(text)

	def getToolsList(self):
		return self.__tools

	def stop(self):
		self.__onStopStrategy.onStop(self.__document)

	def getOnStopStrategy(self):
		return self.__onStopStrategy

	def getDocumtnt(self):
		return self.__document
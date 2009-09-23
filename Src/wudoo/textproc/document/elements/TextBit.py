from wudoo.textproc.document.elements.BaseElement import BaseElement

class TextBit(BaseElement):
	def __init__(self, text):
		BaseElement.__init__(self)
		self.__text = text

	def visit(self, visitor):
		visitor.visitTextBit(self)
	
	def getBuffer(self):
		return self.__text
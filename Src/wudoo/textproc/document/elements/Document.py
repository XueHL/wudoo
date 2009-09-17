from wudoo.textproc.document.elements.BaseCompositElement import BaseCompositElement
from wudoo.textproc.document.elements.NameElement import NameElement

class Document(BaseCompositElement):
	def __init__(self):
		BaseCompositElement.__init__(self)
		self.__bookName = NameElement("Document")

	def getBookName(self):
		return self.__bookName
from wudoo.textproc.document.elements.IHeader import IHeader
from wudoo.textproc.document.elements.BaseElement import BaseElement

class Header(IHeader, BaseElement):
	def __init__(self, level, headerText):
		self.__level = level
		self.__headerText = headerText

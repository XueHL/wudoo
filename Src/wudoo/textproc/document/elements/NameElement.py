from wudoo.textproc.document.elements.INameElement import INameElement

class NameElement(INameElement):
	def __init__(self, name):
		self.__name = name

	def set(self, name):
		self.__name = name
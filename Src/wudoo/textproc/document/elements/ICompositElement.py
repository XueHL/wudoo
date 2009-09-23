from wudoo.textproc.document.elements.IElement import IElement

class ICompositElement(IElement):
	def appendElement(self, element):
		raise NotImplementedError()

	def getElementsList(self):
		raise NotImplementedError()
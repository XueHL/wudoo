from wudoo.textproc.document.elements.IElement import IElement

class IHeader(IElement):
	def getText(self):
		raise NotImplementedError()
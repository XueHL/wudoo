from wudoo.textproc.document.elements.ICompositElement import ICompositElement
from wudoo.textproc.document.elements.BaseElement import BaseElement

class BaseCompositElement(ICompositElement, BaseElement):
	def __init__(self):
		self.__elements = []

	def appendElement(self, element):
		self.__elements.append(element)

	def getElementsList(self):
		return self.__elements
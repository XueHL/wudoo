from wudoo.textproc.save.ISaveVisitor import ISaveVisitor

class TextSaver(ISaveVisitor):
	def __init__(self, file = None):
		self.__file = file

	def setFile(self, file):
		self.__file = file

	def getExtension(self):
		return "txt"

	def visitDocument(self, document):
		self.__visitComposit(document)

	def __visitComposit(self, composit):
		for child in composit.getElementsList():
			child.visit(self)

	def visitHeader(self, header):
		self.__file.write("\n\t")
		self.__file.write(header.getText())
		self.__file.write("\n\n")

	def visitParagraph(self, paragraph):
		self.__visitComposit(paragraph)
		self.__file.write("\n")

	def visitTextBit(self, textBit):
		self.__file.write(textBit.getBuffer())
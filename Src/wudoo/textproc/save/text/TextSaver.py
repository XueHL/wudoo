from wudoo.textproc.save.ISaveVisitor import ISaveVisitor

def splitWithPgWidthLimit(buff, limit):
	result = []
	while len(buff) > 0:
		l = limit
		if l > len(buff):
			l = len(buff)
		bit = buff[:l]
		buff = buff[l:]
		result.append(bit)
	return result

class TextSaver(ISaveVisitor):
	def __init__(self, file = None):
		self.__file = file
		self.__pgWidth = -1

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
		formatted = self.__formatText(textBit.getBuffer())
		self.__file.write(formatted)

	def setPageWidth(self, pgWidth):
		self.__pgWidth = pgWidth

	def __formatText(self, textBuf):
		if self.__pgWidth > -1:
			return "\n".join(splitWithPgWidthLimit(textBuf, self.__pgWidth))
		else:
			return textBuf

class ISaveVisitor:
	def getExtension(self):
		raise NotImplementedError()

	def setFile(self, file):
		raise NotImplementedError()

	def visitDocument(self, document):
		raise NotImplementedError()

	def visitParagraph(self, paragraph):
		raise NotImplementedError()

	def visitTextBit(self, textBit):
		raise NotImplementedError()
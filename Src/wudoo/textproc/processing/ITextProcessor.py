class ITextProcessor:
	def setBookName(self, name):
		raise NotImplementedError()

	def addHeader(self, level, headerText):
		raise NotImplementedError()

	def newParagraph(self):
		raise NotImplementedError()

	def write(self, text):
		raise NotImplementedError()

	def getToolsList(self):
		raise NotImplementedError()

	def stop(self):
		raise NotImplementedError()

	def getDocumtnt(self):
		raise NotImplementedError()
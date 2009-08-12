class ICompilationResult:
	def getObjectFSItems(self):
		raise NotImplementedError()

	def getProject(self):
		raise NotImplementedError()

	def getCompilation(self):
		raise NotImplementedError()
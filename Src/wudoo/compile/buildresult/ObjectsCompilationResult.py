from wudoo.compile.buildresult.BaseCompilationResult import BaseCompilationResult

class ObjectsCompilationResult(BaseCompilationResult):
	def __init__(self, project, compilation):
		BaseCompilationResult.__init__(self, project, compilation)
		self.__objectFSItems = []

	def getObjectFSItems(self):
		return self.__objectFSItems

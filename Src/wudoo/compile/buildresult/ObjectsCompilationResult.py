from wudoo.compile.buildresult.BaseCompilationResult import BaseCompilationResult

class ObjectsCompilationResult(BaseCompilationResult):
	def __init__(self, project):
		BaseCompilationResult.__init__(self, project)
		self.__objectFSItems = []

	def getObjectFSItems(self):
		return self.__objectFSItems

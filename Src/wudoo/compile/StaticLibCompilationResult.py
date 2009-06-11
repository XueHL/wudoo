from wudoo.compile.BaseCompilationResult import BaseCompilationResult

class StaticLibCompilationResult(BaseCompilationResult):
	def __init__(self, project, staticlibFSItem):
		BaseCompilationResult.__init__(self, project)
		self.__staticlibFSItem = staticlibFSItem
		
	def getObjectFSItems(self):
		return [self.__staticlibFSItem]
		
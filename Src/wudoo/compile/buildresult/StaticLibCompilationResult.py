from wudoo.compile.buildresult.BaseCompilationResult import BaseCompilationResult

class StaticLibCompilationResult(BaseCompilationResult):
	def __init__(self, project, staticlibFSItem = None):
		BaseCompilationResult.__init__(self, project)
		self.__staticlibFSItem = staticlibFSItem
		
	def getObjectFSItems(self):
		return [self.__staticlibFSItem]
		
	def setStaticlibFSItem(self, staticlibFSItem):
		self.__staticlibFSItem = staticlibFSItem
		
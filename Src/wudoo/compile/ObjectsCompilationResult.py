from wudoo.compile.ICompilationResult import ICompilationResult

class ObjectsCompilationResult(ICompilationResult):
	def __init__(self):
		self.__objectFSItems = []

	def getObjectFSItems(self):
		return self.__objectFSItems

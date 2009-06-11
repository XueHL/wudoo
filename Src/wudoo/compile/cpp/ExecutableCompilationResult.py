from wudoo.compile.ICompilationResult import ICompilationResult

class ExecutableCompilationResult(ICompilationResult):
	def __init__(self, executableFSItem):
		self.__executableFSItem = executableFSItem

	def getExecutableFSItem(self):
		return self.__executableFSItem
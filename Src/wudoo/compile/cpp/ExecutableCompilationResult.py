from wudoo.compile.buildresult.BaseCompilationResult import BaseCompilationResult

class ExecutableCompilationResult(BaseCompilationResult):
	def __init__(self, project, compilation, executableFSItem):
		BaseCompilationResult.__init__(self, project, compilation)
		self.__executableFSItem = executableFSItem

	def getExecutableFSItem(self):
		return self.__executableFSItem
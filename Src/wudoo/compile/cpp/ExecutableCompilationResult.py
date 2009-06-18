from wudoo.compile.buildresult.BaseCompilationResult import BaseCompilationResult

class ExecutableCompilationResult(BaseCompilationResult):
	def __init__(self, project, executableFSItem):
		BaseCompilationResult.__init__(self, project)
		self.__executableFSItem = executableFSItem

	def getExecutableFSItem(self):
		return self.__executableFSItem
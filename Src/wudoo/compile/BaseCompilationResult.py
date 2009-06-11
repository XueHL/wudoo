from wudoo.compile.ICompilationResult import ICompilationResult

class BaseCompilationResult(ICompilationResult):
	def __init__(self, project):
		self.__project = project

	def getProject(self):
		return self.__project
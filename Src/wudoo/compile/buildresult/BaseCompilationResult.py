from wudoo.compile.buildresult.ICompilationResult import ICompilationResult

class BaseCompilationResult(ICompilationResult):
	def __init__(self, project, compilation):
		self.__project = project
		self.__compilation = compilation

	def getProject(self):
		return self.__project

	def getCompilation(self):
		return self.__compilation
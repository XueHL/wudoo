from wudoo.compile.ICompileResult2builderStrategy import ICompileResult2builderStrategy

class DefaultEmptyCompileResult2builderStrategy(ICompileResult2builderStrategy):
	def __init__(self):
		self.__buildersMap = {}

	def registerBuilder(self, compilationResultClazz, builder):
		self.__buildersMap[compilationResultClazz] = builder
	
	def emptyCompileResult2builder(self, emptyCompilationResult):
		project = emptyCompilationResult.getProject()
		prjBasedBuilder = self.getProjectBasedBuilder(project)
		if prjBasedBuilder is not None:
			return prjBasedBuilder
		return self.__buildersMap[emptyCompilationResult.__class__]

	def getProjectBasedBuilder(self, project):
		try:
			return project.getSpecialBuilder()
		except:
			return None
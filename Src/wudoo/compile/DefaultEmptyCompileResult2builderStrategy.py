from wudoo.compile.ICompileResult2builderStrategy import ICompileResult2builderStrategy

class DefaultEmptyCompileResult2builderStrategy(ICompileResult2builderStrategy):
	def __init__(self):
		self.__buildersMap = {}

	def registerBuilder(self, compilationResultClazz, builder):
		self.__buildersMap[compilationResultClazz] = builder
	
	def emptyCompileResult2builder(self, emptyCompilationResult):
		return self.__buildersMap[emptyCompilationResult.__class__]

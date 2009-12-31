from wudoo.compile.compilationpool.AlwaysRecompileStrategy import AlwaysRecompileStrategy
from wudoo.compile.dependence.IResolveDependenceStrategy import IResolveDependenceStrategy

class BaseResolveDependenceStrategy(IResolveDependenceStrategy):
	def __init__(
			self,
			compilationPoolStrategy = AlwaysRecompileStrategy(),
			):
		self.__compilationPoolStrategy = compilationPoolStrategy 
	
	def getCompilationPoolStrategy(self):
		return self.__compilationPoolStrategy
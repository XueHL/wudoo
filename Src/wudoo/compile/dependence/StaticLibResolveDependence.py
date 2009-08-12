from wudoo.FSItem import FSItem

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.buildresult.StaticLibCompilationResult import StaticLibCompilationResult

class StaticLibResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationPool(),
			)

	def resolve(self, depPrj, rootCompilation, willExecutor):
		compiledResult = self.getCompilationPoolStrategy().findCompiled(
			depPrj,
			rootCompilation,
			self
			)
		if compiledResult is not None:
			return compiledResult
		staticLibCompilationResult = StaticLibCompilationResult(depPrj)
		rootCompilation.buildCompilationResult(staticLibCompilationResult, willExecutor)
		self.getCompilationPoolStrategy().onNewCompiled(staticLibCompilationResult)
		return staticLibCompilationResult

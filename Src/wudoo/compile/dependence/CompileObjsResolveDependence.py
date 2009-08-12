import os

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult

class CompileObjsResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationPool(),
			)

	def resolve(self, depPrj, rootCompilation, willExecutor):
		compilationResult = ObjectsCompilationResult(depPrj)
		rootCompilation.buildCompilationResult(compilationResult, willExecutor)
		self.getCompilationPoolStrategy().onNewCompiled(compilationResult)
		return compilationResult

import os

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult

class CompileObjsResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationaPool(),
			)

	def resolve(self, depPrj, rootCompilation, willExecutor):
		compilationResult = ObjectsCompilationResult(depPrj)
		rootCompilation.buildCompilationResult(compilationResult, willExecutor)
		return compilationResult

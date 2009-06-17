import os

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult

class CompileObjsResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationaPool(),
			)

	def resolve(self, depPrj, rootCompilation, willExecutor):
		return CompileObjsResolveDependence.compileObjsResolve(
			depPrj, 
			rootCompilation, 
			willExecutor,
			self.getCompilationPoolStrategy()										
			)
		
	def __compileObjsResolve(depPrj, rootCompilation, willExecutor, compilationPoolStrategy):
		depPrj.findSources()
		compilationResult = ObjectsCompilationResult(depPrj)
		rootCompilation.buildCompilationResult(compilationResult, willExecutor)
		compilationPoolStrategy.onNewCompiled(compilationResult)
		return compilationResult
	compileObjsResolve = staticmethod(__compileObjsResolve)

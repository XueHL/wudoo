from wudoo.FSItem import FSItem

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.StaticLibCompilationResult import StaticLibCompilationResult

class StaticLibResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationaPool(),
			)

	def resolve(self, depPrj, parentCompilation, willExecutor):
		compiled = self.getCompilationPoolStrategy().findCompiled(
			depPrj,
			parentCompilation
			)
		if compiled is not None:
			return compiled._ggg_archive
		compileObjectsResult = CompileObjsResolveDependence.compileObjsResolve(
			depPrj, 
			parentCompilation, 
			willExecutor,
			self.getCompilationPoolStrategy()
			)
		staticLibFSItem = parentCompilation.getAllocateStrategy().allocateStaticLib(depPrj)
		parentCompilation.getCompiler().archive(
			depPrj, 
			compileObjectsResult, 
			willExecutor, 
			staticLibFSItem
			)
		self.getCompilationPoolStrategy().onNewCompiled(compileObjectsResult)
		return StaticLibCompilationResult(depPrj, staticLibFSItem)

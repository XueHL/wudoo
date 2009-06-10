from wudoo.FSItem import FSItem

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence

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
		compilation = CompileObjsResolveDependence.createDependenceCompilation(
			depPrj, 
			parentCompilation, 
			willExecutor
			)
		if parentCompilation.getDependenceBuildRoot() is not None:
			depRoot = parentCompilation.getDependenceBuildRoot()
		self.__staticLibFSItem = FSItem(
			depRoot, 
			depPrj.getName() + ".a"
			)
		parentCompilation.getCompiler().archive(
			depPrj, 
			compilation, 
			willExecutor, 
			self.__staticLibFSItem
			)
		compilation._ggg_archive = [self.__staticLibFSItem]
		self.getCompilationPoolStrategy().onNewCompiled(compilation)
		return [self.__staticLibFSItem]

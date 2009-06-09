from wudoo.FSItem import FSItem
from wudoo.compile.cpp.dependence.CompiledObjsDependence import CompiledObjsDependence
from wudoo.compile.dependence.IResolveDependenceStrategy import IResolveDependenceStrategy
from wudoo.compile.dependence.BaseDependence import BaseDependence
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool

class StaticLibResolveDependence(IResolveDependenceStrategy, BaseDependence):
	def __init__(self):
		BaseDependence.__init__(self, None, compilationPoolStrategy = StoreCompilationaPool())

	def resolve(self, depPrj, parentCompilation, willExecutor):
		#compiled = self._BaseDependence__searchCompiled(parentCompilation)
		compiled = self.getCompilationPoolStrategy().findCompiled(
			depPrj,
			parentCompilation
			)
		if compiled is not None:
			return compiled._ggg_archive
		compilation = CompiledObjsDependence.createDependenceCompilation(
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

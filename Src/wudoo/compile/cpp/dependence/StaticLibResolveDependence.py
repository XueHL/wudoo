from wudoo.FSItem import FSItem
from wudoo.compile.cpp.dependence.CompiledObjsDependence import CompiledObjsDependence
from wudoo.compile.dependence.IResolveDependenceStrategy import IResolveDependenceStrategy
from wudoo.compile.dependence.BaseDependence import BaseDependence

class StaticLibResolveDependence(IResolveDependenceStrategy, BaseDependence):
	def __init__(self):
		BaseDependence.__init__(self, None)

	def resolve(self, depPrj, parentCompilation, willExecutor):
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
		self.getCompilationPoolStrategy().onNewCompiled(self)
		return [self.__staticLibFSItem]

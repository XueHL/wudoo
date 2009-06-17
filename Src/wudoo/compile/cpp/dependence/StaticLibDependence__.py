from wudoo.FSItem import FSItem
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool

#class StaticLibDependence(BaseDependence):
#	def __init__(
#			self, 
#			project, 
#			buildRoot = None, 
#			compilationPoolStrategy = StoreCompilationaPool()
#			):
#		BaseDependence.__init__(self, project, buildRoot, compilationPoolStrategy)
#		self.__staticLibFSItem = None
#
#	def resolve(self, parentCompilation, willExecutor):
#		compiled = self._BaseDependence__searchCompiled(parentCompilation)
#		if compiled is not None:
#			self.__staticLibFSItem = compiled.getObjectItems()[0]
#			return
#		compilation = CompiledObjsDependence.createDependenceCompilation(
#			self.getProject(), 
#			parentCompilation, 
#			willExecutor
#			)
#		if parentCompilation.getDependenceBuildRoot() is not None:
#			depRoot = parentCompilation.getDependenceBuildRoot()
#		self.__staticLibFSItem = FSItem(
#			depRoot, 
#			self.getProject().getName() + ".a"
#			)
#		parentCompilation.getCompiler().archive(
#			self.getProject(), 
#			compilation, 
#			willExecutor, 
#			self.__staticLibFSItem
#			)
#		self.getCompilationPoolStrategy().onNewCompiled(self)
#
#	def getObjectItems(self):
#		result = []
#		if self.__staticLibFSItem is not None:
#			result.append(self.__staticLibFSItem)
#		return result		
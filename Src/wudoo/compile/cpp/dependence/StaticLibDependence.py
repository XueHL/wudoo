from wudoo.compile.cpp.dependence.CompiledObjsDependence import CompiledObjsDependence
from wudoo.compile.dependence.BaseDependence import BaseDependence
from wudoo.FSItem import FSItem

class StaticLibDependence(BaseDependence):
	def __init__(self, project, buildRoot = None):
		BaseDependence.__init__(self, project, buildRoot)
		self.__staticLibFSItem = None

	def resolve(self, parentCompilation, willExecutor):
		compilation = self._BaseDependence__searchCompiled(parentCompilation)
		if compilation is None:
			compilation = CompiledObjsDependence.createDependenceCompilation(
				self.getProject(), 
				parentCompilation, 
				willExecutor
				)
		if parentCompilation.getDependenceBuildRoot() is not None:
			depRoot = parentCompilation.getDependenceBuildRoot()
		self.__staticLibFSItem = FSItem(
			depRoot, 
			self.getProject().getName() + ".a"
			)
		compilation.getCompiler().archive(
			self.getProject(), 
			compilation, 
			willExecutor, 
			self.__staticLibFSItem
			)

	def getObjectItems(self):
		result = []
		if self.__staticLibFSItem is not None:
			result.append(self.__staticLibFSItem)
		return result		
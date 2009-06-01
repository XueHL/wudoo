from wudoo.compile.cpp.dependency.CompiledObjsDependency import CompiledObjsDependency
from wudoo.compile.dependency.BaseDependency import BaseDependency
from wudoo.FSItem import FSItem

class StaticLibDependency(BaseDependency):
	def __init__(self, project, buildRoot = None):
		BaseDependency.__init__(self, project, buildRoot)
		self.__staticLibFSItem = None

	def resolve(self, parentCompilation, willExecutor):
		compilation = CompiledObjsDependency.createDependencyCompilation(self.getProject(), parentCompilation, willExecutor)
		if parentCompilation.getDependenceBuildRoot() is not None:
			depRoot = parentCompilation.getDependenceBuildRoot()
		self.__staticLibFSItem = FSItem(depRoot, self.getProject().getName() + ".a")
		compilation.getCompiler().archive(self.getProject(), compilation, willExecutor, self.__staticLibFSItem)

	def getObjectItems(self):
		result = []
		if self.__staticLibFSItem is not None:
			result.append(self.__staticLibFSItem)
		return result		
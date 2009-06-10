import os

from wudoo.compile.dependence.BaseResolveDependenceStrategy import BaseResolveDependenceStrategy
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.cpp.CPPCompilation import CPPCompilation

class CompileObjsResolveDependence(BaseResolveDependenceStrategy):
	def __init__(self):
		BaseResolveDependenceStrategy.__init__(
			self,
			compilationPoolStrategy = StoreCompilationaPool(),
			)

	def resolve(self, depPrj, parentCompilation, willExecutor):
		compilation = CompileObjsResolveDependence.createDependenceCompilation(
			depPrj, 
			parentCompilation, 
			willExecutor
			)
		self.getCompilationPoolStrategy().onNewCompiled(compilation)
		return compilation.getAllObjectItems(addEntryPoints = False)


	def __createDependenceCompilation(project, parentCompilation, willExecutor):
		compilation = CPPCompilation(project)
		compilation.setCompiler(parentCompilation.getCompiler())
		if parentCompilation.getDependenceBuildRoot() is not None:
			compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), project.getName()))
		compilation.compile(willExecutor)
		return compilation

	createDependenceCompilation = staticmethod(__createDependenceCompilation)
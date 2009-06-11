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

	def resolve(self, depPrj, parentCompilation, willExecutor):
		compilation = CompileObjsResolveDependence.createDependenceCompilation(
			depPrj, 
			parentCompilation, 
			willExecutor
			)
		self.getCompilationPoolStrategy().onNewCompiled(compilation)
		return compilation.getAllObjectItems(addEntryPoints = False)


	def __createDependenceCompilation(project, parentCompilation, willExecutor):
		from wudoo.compile.cpp.CPPCompilation import CPPCompilation
		#compilation = CPPCompilation(project)
		#compilation.setCompiler(parentCompilation.getCompiler())
		compileResult = ObjectsCompilationResult()
		#if parentCompilation.getDependenceBuildRoot() is not None:
		#	compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), project.getName()))
		parentCompilation.buildCompilationResult(compileResult, willExecutor)
		return compileResult

	createDependenceCompilation = staticmethod(__createDependenceCompilation)
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
		return CompileObjsResolveDependence.compileObjsResolve(
			depPrj, 
			parentCompilation, 
			willExecutor,
			self.getCompilationPoolStrategy()										
			)
		
	def __compileObjsResolve(depPrj, parentCompilation, willExecutor, compilationPoolStrategy):
		#compilation = CompileObjsResolveDependence.createDependenceCompilation(
		#	depPrj, 
		#	parentCompilation, 
		#	willExecutor
		#	)
		#print depPrj.getName()
		#dd()
		depPrj.findSources()
		compilationResult = ObjectsCompilationResult(depPrj)
		parentCompilation.buildCompilationResult(compilationResult, willExecutor)
		compilationPoolStrategy.onNewCompiled(compilationResult)
		#d()
		#return compilation.getAllObjectItems(addEntryPoints = False)
		#print [i.getPathNameExt() for i in compilationResult.getObjectFSItems()]
		return compilationResult
	compileObjsResolve = staticmethod(__compileObjsResolve)


#	def __createDependenceCompilation(project, parentCompilation, willExecutor):
#		from wudoo.compile.cpp.CPPCompilation import CPPCompilation
#		#compilation = CPPCompilation(project)
#		#compilation.setCompiler(parentCompilation.getCompiler())
#		compileResult = ObjectsCompilationResult(project)
#		#if parentCompilation.getDependenceBuildRoot() is not None:
#		#	compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), project.getName()))
#		parentCompilation.buildCompilationResult(compileResult, willExecutor)
#		return compileResult
#
#	createDependenceCompilation = staticmethod(__createDependenceCompilation)
	
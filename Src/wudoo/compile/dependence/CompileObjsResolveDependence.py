from wudoo.compile.dependence.BaseDependence import BaseDependence
from wudoo.compile.dependence.IResolveDependenceStrategy import IResolveDependenceStrategy


class CompileObjsResolveDependence(IResolveDependenceStrategy, BaseDependence):
	def __init__(self):
		BaseDependence.__init__(self, None)

	def resolve(self, depPrj, parentCompilation, willExecutor):
		from wudoo.compile.cpp.dependence.CompiledObjsDependence import CompiledObjsDependence
		compilation = CompiledObjsDependence.createDependenceCompilation(
			depPrj, 
			parentCompilation, 
			willExecutor
			)
		self.getCompilationPoolStrategy().onNewCompiled(self)
		return compilation.getAllObjectItems(addEntryPoints = False)

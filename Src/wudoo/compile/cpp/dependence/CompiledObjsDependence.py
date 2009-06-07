import os

from wudoo.compile.dependence.BaseDependence import BaseDependence
from wudoo.compile.cpp.CPPCompilation import CPPCompilation

class CompiledObjsDependence(BaseDependence):
	def __init__(self, project, buildRoot = None):
		BaseDependence.__init__(self, project, buildRoot)

	def resolve(self, parentCompilation, willExecutor):
#		compilation = self.getCompilationPoolStrategy().searchCompilation(
#			self.getProject(),
#			parentCompilation
#			)
		compilation = None
		if compilation is None:
			compilation = CompiledObjsDependence.createDependenceCompilation(
				self.getProject(), 
				parentCompilation, 
				willExecutor
				)
		self.setDependenceObjects(compilation.getAllObjectItems(addEntryPoints = False))

	def getObjectItems(self):
		return self.getDependenceObjects()

	def __createDependenceCompilation(project, parentCompilation, willExecutor):
		compilation = CPPCompilation(project)
		compilation.setCompiler(parentCompilation.getCompiler())
		#if self.getBuildRoot() is not None:
		#	compilation.setObjRoot(os.path.join(self.getBuildRoot(), project.getName()))
		if parentCompilation.getDependenceBuildRoot() is not None:
			compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), project.getName()))
		compilation.compile(willExecutor)
		#compilation.resolveDependings(willExecutor)
		return compilation

	createDependenceCompilation = staticmethod(__createDependenceCompilation)
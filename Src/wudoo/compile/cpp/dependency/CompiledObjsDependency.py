import os

from wudoo.compile.dependency.BaseDependency import BaseDependency
from wudoo.compile.cpp.CPPCompilation import CPPCompilation

class CompiledObjsDependency(BaseDependency):
	def __init__(self, project, buildRoot = None):
		BaseDependency.__init__(self, project, buildRoot)

	def resolve(self, parentCompilation, willExecutor):
		compilation = CompiledObjsDependency.createDependencyCompilation(self.getProject(), parentCompilation, willExecutor)
		self.setDependenceObjects(compilation.getAllObjectItems(addEntryPoints = False))

	def getObjectItems(self):
		return self.getDependenceObjects()

	def __createDependencyCompilation(project, parentCompilation, willExecutor):
		compilation = CPPCompilation(project)
		compilation.setCompiler(parentCompilation.getCompiler())
		#if self.getBuildRoot() is not None:
		#	compilation.setObjRoot(os.path.join(self.getBuildRoot(), project.getName()))
		if parentCompilation.getDependenceBuildRoot() is not None:
			compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), project.getName()))
		compilation.compile(willExecutor)
		#compilation.resolveDependings(willExecutor)
		return compilation

	createDependencyCompilation = staticmethod(__createDependencyCompilation)
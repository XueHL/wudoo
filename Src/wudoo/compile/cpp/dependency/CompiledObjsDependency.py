import os

from wudoo.compile.dependency.BaseDependency import BaseDependency
from wudoo.compile.cpp.CPPCompilation import CPPCompilation


class CompiledObjsDependency(BaseDependency):
	def __init__(self, project, buildRoot = None):
		BaseDependency.__init__(self, project, buildRoot)

	def resolve(self, parentCompilation, willExecutor):
		p = self.getProject()        
		compilation = CPPCompilation(p)
		compilation.setCompiler(parentCompilation.getCompiler())
		#if self.getBuildRoot() is not None:
		#	compilation.setObjRoot(os.path.join(self.getBuildRoot(), p.getName()))
		if parentCompilation.getDependenceBuildRoot() is not None:
			compilation.setObjRoot(os.path.join(parentCompilation.getDependenceBuildRoot(), p.getName()))
		compilation.compile(willExecutor)
		compilation.resolveDependings(willExecutor)
		self.setDependenceObjects(compilation.getAllObjectItems(addEntryPoints = False))

	def getObjectItems(self):
		return self.getDependenceObjects()
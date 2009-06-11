import os

from wudoo.compile.BaseCompilation import BaseCompilation
#from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.cpp.ExecutableBuilder import ExecutableBuilder
from wudoo.compile.cpp.ObjectsBuilder import ObjectsBuilder

class CPPCompilation(BaseCompilation):
	def __init__(
			self,
			project,
#			objRoot = None
			):
		BaseCompilation.__init__(
			self, 
			project,
			)
#		self.setObjRoot(objRoot)
		self.registerBuilder(
			ExecutableCompilationResult,
			ExecutableBuilder(self)
			)
		self.registerBuilder(
			ObjectsCompilationResult,
			ObjectsBuilder(self)
			)
	
#	def setObjRoot(self, objRoot):
#		if objRoot is None:
#			objRoot = os.path.join(self.getProject().getRoot(), "Out", "Obj")
#		objRoot = os.path.abspath(objRoot)
#		self.setAllocateObjStrategy(AllocInSpecifDirStrategy(objRoot, ".o"))

class Faik:
	def __init__(
			self, 
			project, 
			objRoot = None, 
#			binDestFSItem = None, 
			dependenceBuildRoot = None
			):
		BaseCompilation.__init__(self, project)
		self.setObjRoot(objRoot)
#		self.setBinDestFSItem(binDestFSItem)
		self.setDependenceBuildRoot(dependenceBuildRoot)

	def isEntryPoint(self, fsItem):
		return fsItem.getName().find("main") > -1
	
	def _skipObjectItem(self, src, **params):
		addEntryPoints = "addEntryPoints"
		if not params.has_key(addEntryPoints):
			params[addEntryPoints] = True # default
		return not params[addEntryPoints] and self.isEntryPoint(src)

	def _newCompilation(self, project):
		return CPPCompilation(project)
import os
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy

class CPPCompilation(BaseCompilation):
	def __init__(self, project, objRoot = None, binDestFSItem = None, dependenceBuildRoot = None):
		BaseCompilation.__init__(self, project)
		self.setObjRoot(objRoot)
		self.setBinDestFSItem(binDestFSItem)
		self.setDependenceBuildRoot(dependenceBuildRoot)

	def isEntryPoint(self, fsItem):
		return fsItem.getName().find("main") > -1

	def setObjRoot(self, objRoot):
		if objRoot is None:
			objRoot = os.path.join(self.getProject().getRoot(), "Out", "Obj")
		self.setAllocateObjStrategy(AllocInSpecifDirStrategy(objRoot, ".o"))
    
	def _skipObjectItem(self, src, **params):
		addEntryPoints = "addEntryPoints"
		if not params.has_key(addEntryPoints):
			params[addEntryPoints] = True # default
		return not params[addEntryPoints] and self.isEntryPoint(src)

	def _newCompilation(self, project):
		return CPPCompilation(project)
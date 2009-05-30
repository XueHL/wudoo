import os
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.FSItem import FSItem

class CPPCompilation(BaseCompilation):
	def __init__(self, project, objRoot = None, binDestFSItem = None, dependenceBuildRoot = None):
		BaseCompilation.__init__(self, project)
		self.setObjRoot(objRoot)
		self.setBinDestFSItem(binDestFSItem)
		self.setDependenceBuildRoot(dependenceBuildRoot)
		self.__dependenceObjects = []

	def setObjRoot(self, objRoot):
		if objRoot is None:
			objRoot = os.path.join(self.getProject().getRoot(), "Out", "Obj")
		self.setAllocateObjStrategy(AllocInSpecifDirStrategy(objRoot, ".o"))

	def setBinDestFSItem(self, binDestFSItem):
		if binDestFSItem is None:
			binDestFSItem = FSItem(self.getProject().getRoot(), os.path.join("Out", "Bin"), self.getProject().getName())
		self.setGoalFSItem(binDestFSItem)

	def setDependenceBuildRoot(self, dependenceBuildRoot):
		self.__dependenceBuildRoot = dependenceBuildRoot

	def resolveDependings(self, willExecutor):
		for p in self.getProject().getDependenceProjects():
			compilation = CPPCompilation(p)
			compilation.setCompiler(self.getCompiler())
			if self.__dependenceBuildRoot is not None:
				compilation.setObjRoot(os.path.join(self.__dependenceBuildRoot, p.getName()))
			compilation.compile(willExecutor)
			compilation.resolveDependings(willExecutor)
			self.__dependenceObjects.extend(compilation.getAllObjectItems(addEntryPoints = False))

	def getAllObjectItems(self, addEntryPoints = True):
		result = []
		src2ObjMap = self.getSrc2ObjMap()
		for src in self.getProject().getSourceItems():
			if not addEntryPoints and self.isEntryPoint(src):
				continue
			obj = src2ObjMap[src]
			result.append(obj)
		result.extend(self.__dependenceObjects)
		return result

	def isEntryPoint(self, fsItem):
		return fsItem.getName().find("main") > -1
import os
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.FSItem import FSItem

class CPPCompilation(BaseCompilation):
	def __init__(self, project, objRoot = None, binDestFSItem = None):
		BaseCompilation.__init__(self, project)
		self.setObjRoot(objRoot)
		self.setBinDestFSItem(binDestFSItem)

	def setObjRoot(self, objRoot):
		if objRoot is None:
			objRoot = os.path.join(self.getProject().getRoot(), "Out", "Obj")
		self.setAllocateObjStrategy(AllocInSpecifDirStrategy(objRoot, ".o"))

	def setBinDestFSItem(self, binDestFSItem):
		if binDestFSItem is None:
			binDestFSItem = FSItem(self.getProject().getRoot(), os.path.join("Out", "Bin"), self.getProject().getName())
		self.setGoalFSItem(binDestFSItem)


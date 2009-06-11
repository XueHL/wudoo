import os

from wudoo.FSItem import FSItem
from wudoo.compile.allocate.IAllocateStrategy import IAllocateStrategy

class OutputRootBasedAllocate(IAllocateStrategy):
	def __init__(
			self,
			root,
			objFolder,
			objExt,
			binFolder,
			outerFolder,
			rootProject,
			libext = ".a",
			):
		self.__objFolder = os.path.join(root, objFolder)
		self.__binFolder = os.path.join(root, binFolder)
		self.__outerFolder = os.path.join(root, outerFolder)
		self.__objExt = objExt
		self.__objSubFld = objFolder
		self.__rootProject = rootProject
		self.__libext = libext 
	
	def allocateExecutable(self, project):
		return FSItem(self.__binFolder, project.getName())
		
	def allocateObj(self, src, project):
		if project == self.__rootProject:
			path = [self.__objFolder]
		else:
			path = [os.path.join(self.__outerFolder, self.__objSubFld, project.getName())]
		path.extend(src.getPathArr(1)) 
		path.append(src.getName() + self.__objExt)
		return FSItem(*path)
	
	def allocateStaticLib(self, project):
		return FSItem(self.__outerFolder, project.getName() + self.__libext)
		
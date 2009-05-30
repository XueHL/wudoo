import os
from wudoo.FSItem import FSItem

class DefaultCPPBuildSettings:
	def __init__(self):
		self.__objRoot = None
		self.__exeFileFSItem = None
		self.__dependenceBuildRoot = None

	def setObjRoot(self, objRoot):
		objRoot = os.path.abspath(objRoot)
		self.__objRoot = objRoot

	def setDependenceBuildRoot(self, dependenceBuildRoot):
		dependenceBuildRoot = os.path.abspath(dependenceBuildRoot)
		self.__dependenceBuildRoot = dependenceBuildRoot

	def setExeFile(self, exeFile):
		exeFile = os.path.abspath(exeFile)
		exeFileP = os.path.split(exeFile)[0]
		exeFileN = os.path.split(exeFile)[1]
		self.__exeFileFSItem = FSItem(exeFileP, exeFileN)

	def fillCompilation(self, compilation):
		compilation.setObjRoot(self.__objRoot)
		compilation.setBinDestFSItem(self.__exeFileFSItem)
		compilation.setDependenceBuildRoot(self.__dependenceBuildRoot)

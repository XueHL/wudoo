import os, sys
from wudoo.compile import SourceFilterColl
from wudoo.FSItem import FSItem

class Project:
	"""\
Structure.\
"""
	def __init__(self, rootPath = "", name = None):
		self.setRoot(rootPath)
		self.__sourceFolders = []
		self.__filter = SourceFilterColl.ACCEPT_ALL_FILTER
		self.__sourceItems = []
		if name is None:
			name = self.getRoot().replace("/", "_").replace("\\", "_").replace(":", "_") + ".exe"
		self.__name = name
		self.__dependencePrjs = []
		
	def getName(self):
		return self.__name
		
	def setRoot(self, rootPath, basePath = None):
		if basePath is None:
			basePath = sys.path[0]
		self.__rootPath = os.path.normpath(os.path.join(basePath, rootPath))

	def getRoot(self):
		return self.__rootPath
	
	def setSourceFilter(self, sourceFilter):
		self.__filter = sourceFilter

	def addSrcFolders(self, srcFolder):
		srcFolder = Project.splitSrcDescr(srcFolder)
		self.__sourceFolders.extend(srcFolder)
	
	def getSrcFolders(self):
		return self.__sourceFolders
	
	def findSources(self):
		self.__sourceItems = []
		for srcFold in self.__sourceFolders:
			self.__recFS(srcFold, "")

	def getSourceItems(self):
		return self.__sourceItems
	
	def __recFS(self, srcFold, cur):
		curGl = os.path.join(self.__rootPath, srcFold, cur)
		if os.path.isfile(curGl):
			if self.__filter.accepts(curGl):
				self.__sourceItems.append(FSItem(self.__rootPath, srcFold, cur))
		else:
			for sub in os.listdir(curGl):
				curPr = os.path.join(cur, sub)
				self.__recFS(srcFold, curPr);

	def addDependenceProject(self, depPrj):
		self.__dependencePrjs.append(depPrj)

	def getDependenceProjects(self):
		return self.__dependencePrjs
				
	def __splitSrcDescr(descr):
		descr = descr.split("\n")
		while len(descr) > 0 and len(descr[0]) == 0:
			descr= descr[1:]
		while len(descr) > 0 and len(descr[len(descr) - 1]) == 0:
			descr= descr[:-1]
		return descr
	splitSrcDescr = staticmethod(__splitSrcDescr)
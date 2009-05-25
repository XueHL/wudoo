import os, sys
from wudoo.compile import SourceFilterColl
from wudoo.FSItem import FSItem

class Project:
	def __init__(self, rootPath = ""):
		self.setRoot(rootPath)
		self.__sourceFolders = []
		self.__filter = SourceFilterColl.ACCEPT_ALL_FILTER
		self.__sourceItems = []
		
	def setRoot(self, rootPath):
		self.__rootPath = os.path.normpath(os.path.join(sys.path[0], rootPath))

	def getRoot(self):
		return self.__rootPath
	
	def setSourceFilter(self, sourceFilter):
		self.__filter = sourceFilter

	def addSrcFolders(self, srcFolder):
		self.__sourceFolders.append(srcFolder)
	
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
				
				
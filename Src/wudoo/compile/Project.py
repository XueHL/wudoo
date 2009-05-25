import os, sys

class Project:
	def __init__(self, rootPath = ""):
		self.setRoot(rootPath)
		
	def setRoot(self, rootPath):
		self.rootPath = os.path.normpath(os.path.join(sys.path[0], rootPath))

	def getRoot(self):
		return self.rootPath

	def addSrcFolders(self, srcFolders):
		pass

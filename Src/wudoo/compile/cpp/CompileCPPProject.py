class CompileCPPProject:
	def __init__(self, rootPath = None):
		self.setRoot(rootPath)
		
	def setRoot(self, rootPath):
		self.rootPath = rootPath

	def getRoot(self):
		return self.rootPath

	def addSrcFolders(self, srcFolders):
		pass

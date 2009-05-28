from wudoo.compile.Project import Project
from wudoo.compile import SourceFilterColl 

class CompileCPPProject(Project):
	def __init__(self, rootPath = "", name = None):
		Project.__init__(self, rootPath, name)
		self.setSourceFilter(SourceFilterColl.CPP_SOURCE_FILTER)
		self.__hdrFolders = []
		self.__exportHdrFolders = []

	def addHdrFolders(self, hdrFolders):
		hdrFolders = Project.splitSrcDescr(hdrFolders)
		self.__hdrFolders.extend(hdrFolders)

	def addExportHdrFolders(self, hdrFolders):
		hdrFolders = Project.splitSrcDescr(hdrFolders)
		self.__exportHdrFolders.extend(hdrFolders)

	def getHdrFolders(self):
		return self.__hdrFolders

	def getExportHdrFolders(self):
		return self.__exportHdrFolders
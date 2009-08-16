import os, sys
from wudoo.compile.BaseProject import BaseProject
from wudoo.compile.cpp.ICPPProject import ICPPProject
from wudoo.compile import SourceFilterColl
from wudoo.FSItem import FSItem
from wudoo.fsrecutils import CPPDependUtils

class CPPProject(BaseProject, ICPPProject):
	def __init__(
		self, 
		name,
		moduleFile,
		root = None
		):
		BaseProject.__init__(
			self, 
			name,
			moduleFile,
			root
			)
		self.setSourceFilter(SourceFilterColl.CPP_SOURCE_FILTER)
		self.getEntryPointNames().add("main")
		self.__hdrFolders = []
		self.__exportHdrFolders = []
		
	def addHdrFolders(self, hdrFoldersDescr):
		self.__hdrFolders.extend(BaseProject.reduceFoldersDescr(hdrFoldersDescr))
		
	def addExportHdrFolders(self, exportHhdrFoldersDescr):
		self.__exportHdrFolders.extend(BaseProject.reduceFoldersDescr(exportHhdrFoldersDescr))
		
	def getHdrFolders(self):
		return self.__hdrFolders
		
	def getExportHdrFolders(self):
		return self.__exportHdrFolders

import os

from wudoo.compile.IProject import IProject
from wudoo.fsrecutils import CPPDependUtils
from wudoo.compile import SourceFilterColl

class BaseProject(IProject):
	def __init__(
		self, 
		name,
		moduleFile,
		root = None
		):
		self.__name = name
		moduleFile = os.path.abspath(moduleFile)
		self.__moduleFile = moduleFile
		if root is None:
			root = os.path.normpath(os.path.join(moduleFile, "..", "..")) # reduces CM / <biulder_name.py>
		root = os.path.normpath(root)
		self.__root = root
		
		self.__filter = SourceFilterColl.ACCEPT_ALL_FILTER
		self.__sourceFolders = []
		self.__sourceItems = []
		self.__dependenceProjects = []
		self.__entryPointNames = set()

	def getRoot(self):
		return self.__root
		
	def getName(self):
		return self.__name
	
	def getModuleFile(self):
		return self.__moduleFile
	
	def findSources(self):
		self.__sourceItems = CPPDependUtils.getFilteredFiles(
			self.__root, 
			self.__sourceFolders, 
			self.__filter
			)
		
	def getSourceItems(self):
		return self.__sourceItems
	
	def getDependences(self):
		return self.__dependenceProjects
		
	def addSrcFolders(self, sourceFoldersDescr):
		self.__sourceFolders.extend(BaseProject.reduceFoldersDescr(sourceFoldersDescr))
		
	def addDependenceProject(self, project):
		if project is None:
			raise "project can't be None"
		self.__dependenceProjects.append(project)		
		
	def __reduceFoldersDescr(descr):
		if isinstance(descr, str):
			descr = descr.replace("\t", "").replace(" ", "").split("\n")
		while len(descr[0]) == 0:
			descr = descr[1:]
		while len(descr[len(descr) - 1]) == 0:
			descr = descr[:len(descr) - 1]
		result = []
		for elem in descr:
			if not elem.startswith("#"):
				result.append(elem)
		return result
	reduceFoldersDescr = staticmethod(__reduceFoldersDescr)
	
	def getSrcFolders(self):
		return self.__sourceFolders
		
	def isEntryPointObject(self, objFSItem):
		return objFSItem.getName() in self.__entryPointNames
	
	def getEntryPointNames(self):
		return self.__entryPointNames
	
	def setSourceFilter(self, filter):
		self.__filter = filter

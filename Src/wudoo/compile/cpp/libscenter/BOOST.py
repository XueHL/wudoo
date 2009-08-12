import os

class BoostCommonBuilder:
	def __init__(self, archiveLocation, boostInclude):
		self.__archiveLocation = archiveLocation
		self.__boostInclude = boostInclude

	def build(self, emptyCompilationResult, willExecutor):
		if os.path.exists(self.__boostInclude):
			return
		if not os.path.exists(self.__getBoostIncludeRoot()):
			os.makedirs(self.__getBoostIncludeRoot())
		oldInclContent = set(os.listdir(self.__getBoostIncludeRoot()))
		cmd = "rar x " + self.__archiveLocation + " " + self.__getBoostIncludeRoot()
		os.system(cmd)
		newInclContent = set(os.listdir(self.__getBoostIncludeRoot()))
		includeDir = newInclContent - oldInclContent
		includeDirName = None
		for idn in includeDir:
			includeDirName = idn
		print includeDirName, "\n"
		os.rename(
			os.path.join(self.__getBoostIncludeRoot(), includeDirName),
			self.__boostInclude
		)

	def __getBoostIncludeRoot(self):
		return os.path.split(self.__boostInclude)[0]

class BOOSTCommonLib:
	EMPTY_LIST = []

	def __init__(self):
		self.__moduleFile = __file__
		self.__includeList = ["Include"]

	def getDependences(self):
		return BOOSTCommonLib.EMPTY_LIST

	def getRoot(self):
		return "D:/Other/MPS/_Projects/WuDoo/boost/boost-output"

	def getExportHdrFolders(self):
		return self.__includeList

	def findSources(self):
		pass

	def getSourceItems(self):
		return BOOSTCommonLib.EMPTY_LIST

	def getModuleFile(self):
		return self.__moduleFile

	def getName(self):
		return "BOOST_COMMON_LIB"

	def getSpecialBuilder(self):
		return BoostCommonBuilder("D:/Other/MPS/_Projects/WuDoo/boost/archive/boost_1_39_0.rar", "D:/Other/MPS/_Projects/WuDoo/boost/boost-output/Include")

BOOST_COMMON_LIB = BOOSTCommonLib()

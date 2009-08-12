class HeadersLib:
	EMPTY_LIST = []

	def __init__(self):
		self.__moduleFile = __file__
		self.__includeList = ["Include"]

	def getDependences(self):
		return HeadersLib.EMPTY_LIST

	def getRoot(self):
		return "D:\\/Work/_Outer/Boost/Output/1-39-0/boost-1-39-0-output"

	def getExportHdrFolders(self):
		return self.__includeList

	def findSources(self):
		pass

	def getSourceItems(self):
		return HeadersLib.EMPTY_LIST

	def getModuleFile(self):
		return self.__moduleFile

	def getName(self):
		return "BOOST_HEADERS"

HEADERS_LIB = HeadersLib()

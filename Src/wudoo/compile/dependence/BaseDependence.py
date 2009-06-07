from wudoo.compile.dependence.IDependence import IDependence

class BaseDependence(IDependence):
	def __init__(self, project, buildRoot = None):
		self.__project = project
		self.__buildRoot = buildRoot
		self.__dependenceObjects = []

	def getProject(self):
		return self.__project
	
	def getBuildRoot(self):
		return self.__buildRoot

	def setDependenceObjects(self, dependenceObjects):
		self.__dependenceObjects = dependenceObjects

	def getDependenceObjects(self):
		return self.__dependenceObjects

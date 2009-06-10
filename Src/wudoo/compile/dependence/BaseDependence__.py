from wudoo.compile.dependence.IDependence import IDependence
from wudoo.compile.compilationpool.AlwaysRecompileStrategy import AlwaysRecompileStrategy

class BaseDependence_deleted(IDependence):
	def __init__(
			self, 
			project, 
			buildRoot = None, 
			compilationPoolStrategy = AlwaysRecompileStrategy()
			):
		self.__project = project
		self.__buildRoot = buildRoot
		self.__dependenceObjects = []
		self.__compilationPoolStrategy = compilationPoolStrategy 

	def getProject(self):
		return self.__project
	
	def getBuildRoot(self):
		return self.__buildRoot

	def setDependenceObjects(self, dependenceObjects):
		self.__dependenceObjects = dependenceObjects

	def getDependenceObjects(self):
		return self.__dependenceObjects

	def __searchCompiled(self, parentCompilation):
		return self.__compilationPoolStrategy.findCompiled(
			self.__project,
			parentCompilation
			)
		
	def getCompilationPoolStrategy(self):
		return self.__compilationPoolStrategy
	
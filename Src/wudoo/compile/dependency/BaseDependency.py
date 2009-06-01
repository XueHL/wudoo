from wudoo.compile.dependency.IDependency import IDependency

class BaseDependency(IDependency):
	def __init__(self, project):
		self.__project = project

	def getProject(self):
		return self.__project
	

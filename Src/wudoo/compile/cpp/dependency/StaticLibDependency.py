from wudoo.compile.dependency.BaseDependency import BaseDependency

class StaticLibDependency(BaseDependency):
	def __init__(self, project):
		BaseDependency.__init__(self, project)
		
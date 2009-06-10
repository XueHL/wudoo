class IDependence:
	def getProject(self):
		raise NotImplementedError()

	def resolve(self, parentCompilation, willExecutor):
		raise NotImplementedError()

	def getBuildRoot(self):
		raise NotImplementedError()

	def getDependenceObjects(self):
		raise NotImplementedError()

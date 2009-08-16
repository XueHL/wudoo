class LibsRegOffice:
	def registerLibrary(self, getProjectFunctor):
		projectInstance = getProjectFunctor()
		name = projectInstance.getName()
		moduleFile = projectInstance.getModuleFile()
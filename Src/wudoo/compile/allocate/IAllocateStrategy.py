class IAllocateStrategy:
	def allocateObj(self, src, project):
		raise NotImplementedError()
	
	def allocateExecutable(self, project):
		raise NotImplementedError()
	
	def allocateStaticLib(self, project):
		raise NotImplementedError()

	def allocateSingleProjInfo(self, project, typeStr):
		raise NotImplementedError()
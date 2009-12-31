class IAllocateStrategy:
	def allocateObj(self, src, project):
		raise NotImplementedError()
	
	def allocateExecutable(self, project):
		raise NotImplementedError()
	
	def allocateStaticLib(self, project):
		raise NotImplementedError()

	def allocateSingleCompileInfo(self, typeStr):
		raise NotImplementedError()
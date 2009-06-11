class IAllocateStrategy:
	def allocateObj(self):
		raise NotImplementedError()
	
	def allocateExecutable(self, project):
		raise NotImplementedError()
	
	def allocateStaticLib(self, project):
		raise NotImplementedError()
	
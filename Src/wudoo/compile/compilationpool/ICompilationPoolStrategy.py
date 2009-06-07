class ICompilationPoolStrategy:
	def findCompiled(self, project, parentCompilation):
		raise NotImplementedError()
	
	def onNewCompiled(self, compiledDependence):
		raise NotImplementedError()
	
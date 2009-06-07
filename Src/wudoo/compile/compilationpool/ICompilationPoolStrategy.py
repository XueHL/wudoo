class ICompilationPoolStrategy:
	def findCompiled(self, project, parentCompilation):
		raise NotImplementedError()
	
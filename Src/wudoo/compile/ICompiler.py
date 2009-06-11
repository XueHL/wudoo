class ICompiler:
	def compile(self, src, project, compilation, willExecutor):
		raise NotImplementedError()
	
	def linkExecutable(self, objectFSItems, goalFSItem, willExecutor):
		raise NotImplementedError()
	
	def archive(self, project, compilation, willExecutor):
		raise NotImplementedError()

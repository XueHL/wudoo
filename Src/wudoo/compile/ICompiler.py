class ICompiler:
	def compile(self, src, compilation, willExecutor):
		raise NotImplementedError()
	
	def link(self, project, compilation, willExecutor):
		raise NotImplementedError()
	
	def archive(self, project, compilation, willExecutor):
		raise NotImplementedError()

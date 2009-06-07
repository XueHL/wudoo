from wudoo.compile.compilationpool.ICompilationPoolStrategy import ICompilationPoolStrategy

class AlwaysRecompileStrategy(ICompilationPoolStrategy):
	def findCompiled(self, project, parentCompilation):
		return None

	def onNewCompiled(self, compiledDependence):
		pass

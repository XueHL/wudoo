class ICompilation:
	"""\
Represents a process of compilation.
Stories compilation results that was built.
Holds compiler.
Stories compilation flags.
"""
	def buildCompilationResult(self, emptyCompilationResult, willExecutor):
		raise NotImplementedError()
		
	def registerBuilder(self, compilationResultClazz, builder):
		raise NotImplementedError()

	def setCompiler(self, compiler):
		raise NotImplementedError()
		
	def setResolveDependenceStrategy(self, resolveDependenceStrategy):
		raise NotImplementedError()
		
	def getResolveDependenceStrategy(self):
		raise NotImplementedError()

	def getCompiler(self):
		raise NotImplementedError()
	
	def getAllocateStrategy(self):
		raise NotImplementedError()
	
	def setAllocateStrategy(self, allocateStrategy):
		raise NotImplementedError()

	def setDebugInfoLevel(self, debugInfoLevel):
		"""\
debugInfoLevel in [0 .. 100]
"""		
		raise NotImplementedError()

	def setOptimisationLevel(self, optimisationLevel):
		"""\
optimisationLevel in [0 .. 100]
"""		
		raise NotImplementedError()

	def getDebugInfoLevel(self):
		raise NotImplementedError()

	def getOptimisationLevel(self):
		raise NotImplementedError()

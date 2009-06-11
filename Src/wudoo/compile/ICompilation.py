class ICompilation:
	"""\
Represents a process of compilation.
Stories compilation results that was built.
Holds compiler.
Stories compilation flags.
"""
#	def buildWorkFlow(self, willExecutor):
#		raise NotImplementedError()

#	def getProject(self):
#		raise NotImplementedError()
	
	def buildCompilationResult(self, emptyCompilationResult, willExecutor):
		"""\
emptyCompilationResult - comp result with set destination ... 
but not set obj-s, lib-s, dll-s ...
"""
		raise NotImplementedError()
	
	def getAllocateStrategy(self):
	    raise NotImplementedError()
	
	def setAllocateStrategy(self, allocateStrategy):
	    raise NotImplementedError()
	   	
#	def resolveDependings(self, willExecutor):
#		raise NotImplementedError()

#	def buildBinary(self, willExecutor):
#		raise NotImplementedError()

#	def getAllObjectItems(self, **params):
#		raise NotImplementedError()

#	def getSrc2ObjMap(self):
#		raise NotImplementedError()
	
	def getCompiler(self):
		raise NotImplementedError()

	def setCompiler(self, compiler):
		raise NotImplementedError()

	def setResolveDependenceStrategy(self, resolveDependenceStrategy):
		raise NotImplementedError()

	def getResolveDependenceStrategy(self):
		raise NotImplementedError()
	
#	def setObjRoot(self, objRoot):
#		raise NotImplementedError()

#	def setAllocateObjStrategy(self, strat):
#		raise NotImplementedError()

#	def setDependenceBuildRoot(self, dependenceBuildRoot):
#		raise NotImplementedError()
	
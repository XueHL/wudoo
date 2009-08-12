import os

from wudoo.FSItem import FSItem

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.buildresult.skipcompile.CompileAllStrategy import CompileAllStrategy
from wudoo.compile.DefaultEmptyCompileResult2builderStrategy import DefaultEmptyCompileResult2builderStrategy

class BaseCompilation(ICompilation):
	def __init__(self, project, *faik0, **faik1):
		self.__compiler = None
		self.__allocateStrategy = None
		self.__resolveDependenceStrategy = CompileObjsResolveDependence()
		#self.__buildersMap = {}
		self.__debugInfoLevel = 0
		self.__optimisationLevel = 100
		self.__skipItemsStrategy = CompileAllStrategy()
		self.__emptyCompileResult2builderStrategy = DefaultEmptyCompileResult2builderStrategy()
		
	def buildCompilationResult(self, emptyCompilationResult, willExecutor):
		#builder = self.__buildersMap[emptyCompilationResult.__class__]
		builder = self.__emptyCompileResult2builderStrategy.emptyCompileResult2builder(emptyCompilationResult)
		builder.build(emptyCompilationResult, self, willExecutor)
		
	#def registerBuilder(self, compilationResultClazz, builder):
	#	self.__buildersMap[compilationResultClazz] = builder

	def setCompiler(self, compiler):
		self.__compiler = compiler
		
	def setResolveDependenceStrategy(self, resolveDependenceStrategy):
		self.__resolveDependenceStrategy = resolveDependenceStrategy
		
	def getResolveDependenceStrategy(self):
		return self.__resolveDependenceStrategy

	def getCompiler(self):
		return self.__compiler
	
	def getAllocateStrategy(self):
		return self.__allocateStrategy
	
	def setAllocateStrategy(self, allocateStrategy):
		self.__allocateStrategy = allocateStrategy

	def setDebugInfoLevel(self, debugInfoLevel):
		self.__debugInfoLevel = debugInfoLevel

	def getDebugInfoLevel(self):
		return self.__debugInfoLevel

	def setOptimisationLevel(self, optimisationLevel):
		self.__optimisationLevel = optimisationLevel

	def getOptimisationLevel(self):
		return self.__optimisationLevel

	def setSkipItemsStrategy(self, skipItemsStrategy):
		self.__skipItemsStrategy = skipItemsStrategy

	def getSkipItemsStrategy(self):
		return self.__skipItemsStrategy

	def getEmptyCompileResult2builderStrategy(self):
		return self.__emptyCompileResult2builderStrategy
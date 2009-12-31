import os

from wudoo.FSItem import FSItem

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.buildresult.skipcompile.CompileAllStrategy import CompileAllStrategy
from wudoo.compile.DefaultEmptyCompileResult2builderStrategy import DefaultEmptyCompileResult2builderStrategy
from wudoo.fsrecutils import CPPDependUtils
from wudoo.compile.IProject import IProject

class BaseCompilation(ICompilation):
	def __init__(self, projectSearcher = None, libsRegOffice = None):
		if projectSearcher is None:
			projectSearcher = self
		self.__compiler = None
		self.__allocateStrategy = None
		self.__resolveDependenceStrategy = CompileObjsResolveDependence()
		self.__debugInfoLevel = 0
		self.__optimisationLevel = 100
		self.__skipItemsStrategy = CompileAllStrategy()
		self.__emptyCompileResult2builderStrategy = DefaultEmptyCompileResult2builderStrategy()
		self.__projectSearcher = projectSearcher
		self.__libsRegOffice = libsRegOffice
		
	def buildCompilationResult(self, emptyCompilationResult, willExecutor):
		project = emptyCompilationResult.getProject()
		CPPDependUtils.substituteAllProjects(project, self.__projectSearcher)
		builder = self.__emptyCompileResult2builderStrategy.emptyCompileResult2builder(emptyCompilationResult)
		builder.build(emptyCompilationResult, willExecutor)
		
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

	def searchProject(self, projectDescr):
		if isinstance(projectDescr, IProject):
			return projectDescr
		if (isinstance(projectDescr, str)):
			if self.__libsRegOffice is not None:
				return self.__libsRegOffice.libByName(projectDescr)
		return None

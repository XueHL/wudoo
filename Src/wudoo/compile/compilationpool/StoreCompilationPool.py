import os, pickle

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.compilationpool.ICompilationPoolStrategy import ICompilationPoolStrategy
from wudoo.compile.buildresult.ICompilationResult import ICompilationResult

class StoreCompilationPool(ICompilationPoolStrategy):
	POOL_EXT = ".compilations" 
	COMPILE_SATISFACTION_MAP = None

	def __init__(self):
		if StoreCompilationPool.COMPILE_SATISFACTION_MAP is None:
			from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence
			from wudoo.compile.buildresult.StaticLibCompilationResult import StaticLibCompilationResult
			from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
			from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
			StoreCompilationPool.COMPILE_SATISFACTION_MAP = {
				StaticLibResolveDependence: set([StaticLibCompilationResult]),
				CompileObjsResolveDependence: set([ObjectsCompilationResult]),
			}
	
	def findCompiled(self, project, rootCompilation, resolveDependenceStrat):
		try:
			poolFile = self.__getPoolFile(project)
			if not os.path.exists(poolFile):
				return None
			buf = open(poolFile, "rb").read()
			prevCompileResult = pickle.loads(buf)
			if issubclass(prevCompileResult.__class__, ICompilationResult):
				if self.__isResultSatisfyes(rootCompilation, resolveDependenceStrat, prevCompileResult):
					return prevCompileResult
		except:
			return None
		return None
	
	def onNewCompiled(self, compilationResult):
		poolFile = self.__getPoolFile(compilationResult.getProject())
		if poolFile is None:
			return
		buf = pickle.dumps(compilationResult)
		if not os.path.exists(os.path.split(poolFile)[0]):
			os.makedirs(os.path.split(poolFile)[0])
		stream = open(poolFile, "wb")
		stream.write(buf)
		stream.close()
	
	def __getPoolFile(self, project):
		if project.getModuleFile() is None:
			return None
		moduleDir = os.path.split(project.getModuleFile())[0]
		poolFile = os.path.join(moduleDir, project.getName() + StoreCompilationPool.POOL_EXT)
		return poolFile
	
	def __isResultSatisfyes(self, rootCompilation, resolveDependenceStrat, prevCompileResult):
		try:
			satisfResults = StoreCompilationPool.COMPILE_SATISFACTION_MAP[resolveDependenceStrat.__class__]
			return prevCompileResult.__class__ in satisfResults
		except:
			return False
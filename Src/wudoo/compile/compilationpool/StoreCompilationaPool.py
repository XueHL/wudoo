import os, pickle

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.compilationpool.ICompilationPoolStrategy import ICompilationPoolStrategy
from wudoo.compile.buildresult.ICompilationResult import ICompilationResult

class StoreCompilationaPool(ICompilationPoolStrategy):
	POOL_EXT = ".compilations" 
	
	def findCompiled(self, project, parentCompilation):
		try:
			poolFile = self.__getPoolFile(project)
			if not os.path.exists(poolFile):
				return None
			buf = open(poolFile, "rb").read()
			compilation = pickle.loads(buf)
			if issubclass(compilation.__class__, ICompilationResult):
				if self.__compareCompileFlags(compilation, parentCompilation):
					return compilation
		except:
			return None
		return None
	
	def onNewCompiled(self, compilationResult):
		poolFile = self.__getPoolFile(compilationResult.getProject())
		if poolFile is None:
			return
		buf = pickle.dumps(compilationResult)
		stream = open(poolFile, "wb")
		stream.write(buf)
		stream.close()
	
	def __getPoolFile(self, project):
		if project.getModuleFile() is None:
			return None
		moduleDir = os.path.split(project.getModuleFile())[0]
		poolFile = os.path.join(moduleDir, project.getName() + StoreCompilationaPool.POOL_EXT)
		return poolFile
	
	def __compareCompileFlags(self, compiledDependence, parentcompiledDependence):
		return True
import os, pickle

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.compilationpool.ICompilationPoolStrategy import ICompilationPoolStrategy

class StoreCompilationaPool(ICompilationPoolStrategy):
	POOL_EXT = ".compilations" 
	
	def findCompiled(self, project, parentCompilation):
		try:
			poolFile = self.__getPoolFile(project)
			if not os.path.exists(poolFile):
				return None
			buf = open(poolFile, "rb").read()
			compilation = pickle.loads(buf)
			if issubclass(compilation.__class__, ICompilation):
				if self.__compareCompileFlags(compilation, parentCompilation):
					return compilation
		except:
			return None
		return None
	
	def onNewCompiled(self, compilation):
		poolFile = self.__getPoolFile(compilation.getProject())
		if poolFile is None:
			return
		buf = pickle.dumps(compilation)
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
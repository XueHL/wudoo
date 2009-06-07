import os, pickle

from wudoo.compile.dependence.IDependence import IDependence
from wudoo.compile.compilationpool.ICompilationPoolStrategy import ICompilationPoolStrategy

class StoreCompilationaPool(ICompilationPoolStrategy):
	POOL_EXT = ".compilations" 
	
	def findCompiled(self, project, parentCompilation):
		try:
			poolFile = self.__getPoolFile(project)
			if not os.path.exists(poolFile):
				return None
			buf = open(poolFile, "rb").read()
			compiledDependence = pickle.loads(buf)
			if issubclass(compiledDependence.__class__, IDependence):
				if self.__compareCompileFlags(compiledDependence, parentCompilation):
					return compiledDependence
		except:
			return None
		return None
	
	def onNewCompiled(self, compiledDependence):
		poolFile = self.__getPoolFile(compiledDependence.getProject())
		if poolFile is None:
			return
		buf = pickle.dumps(compiledDependence)
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
from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.ObjectsBuilder import ObjectsBuilder

class ExecutableBuilder(IBuilder):
	def build(self, emptyCompilationResult, willExecutor):
		compilation = emptyCompilationResult.getCompilation()
		project = emptyCompilationResult.getProject()
		objectsCompilationResult = ObjectsCompilationResult(project, compilation)
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems = objectsCompilationResult.getObjectFSItems()

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		for depPrj in self.__allDeps(project):
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			for depObjFSItem in resolveCompilationResult.getObjectFSItems():
				if not depPrj.isEntryPointObject(depObjFSItem):
					objFSItems.append(depObjFSItem)
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)

	def __allDeps(self, project):
		result = []
		result += project.getDependences()
		for dep in project.getDependences():
			result += self.__allDeps(dep)
		return result
			
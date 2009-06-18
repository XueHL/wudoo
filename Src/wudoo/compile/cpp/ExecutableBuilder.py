from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.ObjectsBuilder import ObjectsBuilder

class ExecutableBuilder(IBuilder):
	def build(self, emptyCompilationResult, compilation, willExecutor):
		objectsCompilationResult = ObjectsCompilationResult(emptyCompilationResult.getProject())
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems = objectsCompilationResult.getObjectFSItems()

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		project = emptyCompilationResult.getProject()
		for depPrj in project.getDependences():
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			for depObjFSItem in resolveCompilationResult.getObjectFSItems():
				if not depPrj.isEntryPointObject(depObjFSItem):
					objFSItems.append(depObjFSItem)
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)

from wudoo.compile.BaseBuilder import BaseBuilder
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.cpp.ObjectsBuilder import ObjectsBuilder

class ExecutableBuilder(BaseBuilder):
	def __init__(self, compilation):
		BaseBuilder.__init__(self, compilation)
		
	def build(self, emptyCompilationResult, compilation, willExecutor):
		objectsCompilationResult = ObjectsCompilationResult()
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems = objectsCompilationResult.getObjectFSItems()

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		project = compilation.getProject()
		for depPrj in project.getDependences():
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			objFSItems.extend(resolveCompilationResult.getObjectFSItems())
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)
from wudoo.compile.BaseBuilder import BaseBuilder
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.cpp.ObjectsBuilder import ObjectsBuilder

class ExecutableBuilder(BaseBuilder):
	def __init__(self, compilation):
		BaseBuilder.__init__(self, compilation)
		
	def build(self, emptyCompilationResult, compilation, willExecutor):
		objectsCompilationResult = ObjectsCompilationResult(emptyCompilationResult.getProject())
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems = objectsCompilationResult.getObjectFSItems()

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		project = emptyCompilationResult.getProject()
		for depPrj in project.getDependences():
			#print project.getName(), " ||| ", depPrj.getName()
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			for depObjFSItem in resolveCompilationResult.getObjectFSItems():
				if not depPrj.isEntryPointObject(depObjFSItem):
					objFSItems.append(depObjFSItem)
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)
from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.ObjectsBuilder import ObjectsBuilder
from wudoo.fsrecutils import CPPDependUtils
from wudoo.compile.libscenter.IProjectSearcher import IProjectSearcher

class ExecutableBuilder(IBuilder, IProjectSearcher):
	def __init__(self, substituteProjectsStrategy = None):
		if substituteProjectsStrategy is None:
			substituteProjectsStrategy = self
		self.__projectSearcher = substituteProjectsStrategy
	
	def build(self, emptyCompilationResult, willExecutor):
		compilation = emptyCompilationResult.getCompilation()
		project = emptyCompilationResult.getProject()
		objectsCompilationResult = ObjectsCompilationResult(project, compilation)
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems = objectsCompilationResult.getObjectFSItems()

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		dependProjects = CPPDependUtils.getAllDependProjects(project)
		for depPrj in dependProjects:
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			for depObjFSItem in resolveCompilationResult.getObjectFSItems():
				if not depPrj.isEntryPointObject(depObjFSItem):
					objFSItems.append(depObjFSItem)
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)

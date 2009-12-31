from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.ObjectsBuilder import ObjectsBuilder
from wudoo.fsrecutils import CPPDependUtils
from wudoo.compile.libscenter.IProjectSearcher import IProjectSearcher
from wudoo.compile.cpp.ObjectFSItem import ObjectFSItem
from wudoo.compile.cpp.ArchiveFSItem import ArchiveFSItem


class ExecutableBuilder(IBuilder, IProjectSearcher):
	def __init__(self, substituteProjectsStrategy = None):
		if substituteProjectsStrategy is None:
			substituteProjectsStrategy = self
		self.__projectSearcher = substituteProjectsStrategy
	
	def build(self, emptyCompilationResult, willExecutor):
		compilation = emptyCompilationResult.getCompilation()
		project = emptyCompilationResult.getProject()
		objFSItems = [] 

		resolveDependenceStrategy = compilation.getResolveDependenceStrategy()
		dependProjects = CPPDependUtils.getAllDependProjects(project)
		for depPrj in dependProjects:
			resolveCompilationResult = resolveDependenceStrategy.resolve(depPrj, compilation, willExecutor)
			for depObjFSItem in resolveCompilationResult.getObjectFSItems():
				if not depPrj.isEntryPointObject(depObjFSItem):
					objFSItems.append(depObjFSItem)
					
		objectsCompilationResult = ObjectsCompilationResult(project, compilation)
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		objFSItems.extend(objectsCompilationResult.getObjectFSItems())
		
		objFSItems.sort(cmp = self)
		
		compilation.getCompiler().linkExecutable(objFSItems, emptyCompilationResult.getExecutableFSItem(), willExecutor)

	def __call__(self, fsitemA, fsitemB):
		aiso = isinstance(fsitemA, ObjectFSItem)
		biso = isinstance(fsitemB, ObjectFSItem)
		if aiso and not biso:
			return -1
		if biso and not aiso:
			return 1
		return 0

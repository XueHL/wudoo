from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult

class StaticLibBuilder(IBuilder):
	def build(self, emptyCompilationResult, compilation, willExecutor):
		project = emptyCompilationResult.getProject()
		objectsCompilationResult = ObjectsCompilationResult(project)
		compilation.buildCompilationResult(objectsCompilationResult, willExecutor)
		staticLibFSItem = compilation.getAllocateStrategy().allocateStaticLib(project)
		compilation.getCompiler().archive(
			project, 
			objectsCompilationResult, 
			willExecutor, 
			staticLibFSItem
			)
		emptyCompilationResult.setStaticlibFSItem(staticLibFSItem)
			
		

from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult

class ObjectsBuilder(IBuilder):
	def build(self, emptyCompilationResult, compilation, willExecutor):
		project = emptyCompilationResult.getProject()
		project.findSources()
		compiler = compilation.getCompiler()
		for src in project.getSourceItems():
			compiler.compile(src, project, compilation, willExecutor)
			obj = compilation.getAllocateStrategy().allocateObj(src, emptyCompilationResult.getProject())
			emptyCompilationResult.getObjectFSItems().append(obj)

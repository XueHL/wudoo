from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.skipcompile.CompileAllStrategy import CompileAllStrategy

class ObjectsBuilder(IBuilder):
	def build(self, emptyCompilationResult, willExecutor):
		project = emptyCompilationResult.getProject()
		compilation = emptyCompilationResult.getCompilation()
		project.findSources()
		compiler = compilation.getCompiler()
		skipItemsStrategy = compilation.getSkipItemsStrategy()
		for src in project.getSourceItems():
			obj = compilation.getAllocateStrategy().allocateObj(src, project)
			if not skipItemsStrategy.skip(src, compilation, project):
				compiler.compile(src, obj, project, compilation, willExecutor)
				skipItemsStrategy.onCompiled(src, compilation, project)
			obj = compilation.getAllocateStrategy().allocateObj(src, emptyCompilationResult.getProject())
			emptyCompilationResult.getObjectFSItems().append(obj)

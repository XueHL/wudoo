from wudoo.compile.buildresult.IBuilder import IBuilder
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.skipcompile.CompileAllStrategy import CompileAllStrategy

class ObjectsBuilder(IBuilder):
	def __init__(self, skipItemsStrategy = CompileAllStrategy()):
		self.__skipItemsStrategy = skipItemsStrategy
	
	def build(self, emptyCompilationResult, willExecutor):
		project = emptyCompilationResult.getProject()
		compilation = emptyCompilationResult.getCompilation()
		project.findSources()
		compiler = compilation.getCompiler()
		for src in project.getSourceItems():
			obj = compilation.getAllocateStrategy().allocateObj(src, project)
			if not self.__skipItemsStrategy.skip(src, compilation, project):
				compiler.compile(src, obj, project, compilation, willExecutor)
				self.__skipItemsStrategy.onCompiled(src, compilation, project)
			obj = compilation.getAllocateStrategy().allocateObj(src, emptyCompilationResult.getProject())
			emptyCompilationResult.getObjectFSItems().append(obj)

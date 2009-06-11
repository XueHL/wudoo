from wudoo.compile.BaseBuilder import BaseBuilder
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult

class ObjectsBuilder(BaseBuilder):
	def __init__(self, compilation):
		BaseBuilder.__init__(self, compilation)
		
	def build(self, emptyCompilationResult, compilation, willExecutor):
		project = compilation.getProject()
		compiler = compilation.getCompiler()
		for src in project.getSourceItems():
			compiler.compile(src, compilation, willExecutor)
			obj = compilation.getSrc2ObjMap()[src]
			emptyCompilationResult.getObjectFSItems().append(obj)
			
		

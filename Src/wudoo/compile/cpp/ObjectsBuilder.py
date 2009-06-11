from wudoo.compile.BaseBuilder import BaseBuilder
from wudoo.compile.ObjectsCompilationResult import ObjectsCompilationResult

class ObjectsBuilder(BaseBuilder):
	def __init__(self, compilation):
		BaseBuilder.__init__(self, compilation)
		
	def build(self, emptyCompilationResult, compilation, willExecutor):
		project = emptyCompilationResult.getProject()
		compiler = compilation.getCompiler()
		#print "!!", project.getSourceItems()
		for src in project.getSourceItems():
			compiler.compile(src, project, compilation, willExecutor)
			obj = compilation.getAllocateStrategy().allocateObj(src, emptyCompilationResult.getProject())
			emptyCompilationResult.getObjectFSItems().append(obj)
			
		

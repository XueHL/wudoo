from wudoo.compile.BaseCompiler import BaseCompiler
from wudoo.compile.CreateDestOnPreCompile import CreateDestOnPreCompile

class GPPCompiler(BaseCompiler):
	GPP_Compiler_CMD = "g++"

	def __init__(self, preCompileStrategy = CreateDestOnPreCompile()):
		BaseCompiler.__init__(self)
		self.__gppCmd = GPPCompiler.GPP_Compiler_CMD
		self.__preCompileStrategy = preCompileStrategy

	def compile(self, src, compilation, willExecutor):
		obj = compilation.getSrc2ObjMap()[src]
		command = self.__gppCmd + \
			" -c " + \
			src.getPathNameExt() + \
			" -o " + \
			obj.getPathNameExt() + \
			""
		self.__preCompileStrategy.onPreCompile(obj)
		willExecutor.execute(command)
	
	def link(self, project, compilation, willExecutor, goalFSItem):
		objStr = ""
		for src in project.getSourceItems():
			obj = compilation.getSrc2ObjMap()[src]
			objStr += " " + obj.getPathNameExt()
		command = self.__gppCmd + \
			objStr + \
			" -o " + \
			goalFSItem.getPathNameExt() + \
			""
		self.__preCompileStrategy.onPreLink(goalFSItem)
		willExecutor.execute(command)
			
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

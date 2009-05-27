from wudoo.compile.BaseCompiler import BaseCompiler

class GPPCompiler(BaseCompiler):
	GPP_Compiler_CMD = "g++"

	def __init__(self):
		BaseCompiler.__init__(self)
		self.__gppCmd = GPPCompiler.GPP_Compiler_CMD

	def compile(self, src, compilation, willExecutor):
		obj = compilation.getSrc2ObjMap()[src]
		command = self.__gppCmd + \
			" -c " + \
			src.getPathNameExt() + \
			" -o " + \
			obj.getPathNameExt() + \
			""
		willExecutor.execute(command)

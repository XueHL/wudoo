from wudoo.compile.BaseCompiler import BaseCompiler

class GPPCompiler(BaseCompiler):
	GPP_Compiler_CMD = "g++"

	def __init__(self, willExecutor):
		BaseCompiler.__init__(self, willExecutor = willExecutor)
		self.__gppCmd = GPPCompiler.GPP_Compiler_CMD

	def compile(self, src, obj):
		command = self.__gppCmd + \
			" -c " + \
			src + \
			" -o " + \
			obj + \
			""
		self.getWillExecutor().execute(command)

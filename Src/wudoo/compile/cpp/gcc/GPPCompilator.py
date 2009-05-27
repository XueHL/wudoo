from wudoo.compile.BaseCompilator import BaseCompilator

class GPPCompilator(BaseCompilator):
	GPP_COMPILATOR_CMD = "g++"

	def __init__(self, willExecutor):
		BaseCompilator.__init__(self, willExecutor = willExecutor)
		self.__gppCmd = GPPCompilator.GPP_COMPILATOR_CMD

	def compile(self, src, obj):
		command = self.__gppCmd + \
			" -c " + \
			src + \
			" -o " + \
			obj + \
			""
		self.getWillExecutor().execute(command)

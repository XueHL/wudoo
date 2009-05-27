from wudoo.compile.ICompiler import ICompiler

class BaseCompiler(ICompiler):
	def __init__(self, willExecutor):
		self.__willExecutor = willExecutor

	def getWillExecutor(self):
		return self.__willExecutor
from wudoo.compile.ICompilator import ICompilator

class BaseCompilator(ICompilator):
	def __init__(self, willExecutor):
		self.__willExecutor = willExecutor

	def getWillExecutor(self):
		return self.__willExecutor
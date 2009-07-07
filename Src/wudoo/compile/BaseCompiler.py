from wudoo.compile.ICompiler import ICompiler
from wudoo.compile.CompileAllStrategy import CompileAllStrategy

class BaseCompiler(ICompiler):
	def __init__(self, skipItemsStrategy = CompileAllStrategy()):
		self.__skipItemsStrategy = skipItemsStrategy
	
	def getSkipItemsStrategy(self):
		return self.__skipItemsStrategy

import os

from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult
from wudoo.compile.buildresult.ObjectsCompilationResult import ObjectsCompilationResult
from wudoo.compile.buildresult.StaticLibCompilationResult import StaticLibCompilationResult
from wudoo.compile.cpp.ExecutableBuilder import ExecutableBuilder
from wudoo.compile.buildresult.ObjectsBuilder import ObjectsBuilder
from wudoo.compile.buildresult.StaticLibBuilder import StaticLibBuilder

class CPPCompilation(BaseCompilation):
	def __init__(
			self,
			project,
			):
		BaseCompilation.__init__(
			self, 
			project,
			)
		self.registerBuilder(
			ExecutableCompilationResult,
			ExecutableBuilder()
			)
		self.registerBuilder(
			ObjectsCompilationResult,
			ObjectsBuilder()
			)
		self.registerBuilder(
			StaticLibCompilationResult,
			StaticLibBuilder()
			)

import build_sufstring
from wudoo.compile.cpp.Front import *

sufstringProject = build_sufstring.getProject()
compilation = DefaultCPPCompilation()
profilesChain(compilation, sufstringProject)
compilationResult = StaticLibCompilationResult(
	sufstringProject,
	compilation,
	compilation.getAllocateStrategy().allocateStaticLib(sufstringProject)
	)
compilation.buildCompilationResult(compilationResult, SystemWillExecutor())

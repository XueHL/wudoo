import os
from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.DefaultCPPBuildSettings import DefaultCPPBuildSettings
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler

Project = CompileCPPProject
DefaultBuildSettings = DefaultCPPBuildSettings

def DefaultCPPCompilation(project):
	compilation = CPPCompilation(project) 
	compilation.setCompiler(GPPCompiler())
	return compilation

def wdefaultBuild(project):
	compilation = DefaultCPPCompilation(project)
	compilation.compile()
	writeCompilation(compilation)
#	compilation.setGoal(settings.getGoal())
#	compilation.setOutputDir(settings.getOutputDir())
#	compilation.setObjDir(settings.getObjDir())
#	compilation.setBinDir(settings.getBinDir())
	
def writeCompilation(compilation):
	pass

def moduleFile2basePath(modFile):
	return os.path.normpath(os.path.join(modFile, ".."))	
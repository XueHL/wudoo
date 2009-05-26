import os
from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.DefaultCPPBuildSettings import DefaultCPPBuildSettings

Project = CompileCPPProject
DefaultBuildSettings = DefaultCPPBuildSettings

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
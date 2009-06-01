import os, sys

from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.DefaultCPPBuildSettings import DefaultCPPBuildSettings
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.dependency.StaticLibDependency import StaticLibDependency
from wudoo.compile.cpp.dependency.CompiledObjsDependency import CompiledObjsDependency

from wudoo.SystemWillExecutor import SystemWillExecutor

DEPENT_MODULE_PATH_STORRAGE = {}

Project = CompileCPPProject
DefaultBuildSettings = DefaultCPPBuildSettings

def DefaultCPPCompilation(project, objRoot = None, binDestFSItem = None):
	compilation = CPPCompilation(project, objRoot = objRoot, binDestFSItem = binDestFSItem) 
	compilation.setCompiler(GPPCompiler())
	return compilation

def wdefaultBuild(project, settings = DefaultCPPBuildSettings()):
	compilation = DefaultCPPCompilation(project)
	settings.fillCompilation(compilation)
	we = SystemWillExecutor()
	compilation.compile(we)
	compilation.resolveDependings(we)
	compilation.buildBinary(we)
	writeCompilation(compilation)
#	compilation.setGoal(settings.getGoal())
#	compilation.setOutputDir(settings.getOutputDir())
#	compilation.setObjDir(settings.getObjDir())
#	compilation.setBinDir(settings.getBinDir())
	
def writeCompilation(compilation):
	pass

def moduleFile2basePath(modFile):
	return os.path.abspath(os.path.normpath(os.path.join(modFile, "..")))

def addDependProjDir(dppdPath):
	dppdPath = os.path.normpath(dppdPath)
	if not DEPENT_MODULE_PATH_STORRAGE.has_key(dppdPath):
		DEPENT_MODULE_PATH_STORRAGE[dppdPath] = dppdPath
		sys.path.append(dppdPath)

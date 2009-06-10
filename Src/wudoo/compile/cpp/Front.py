import os, sys

from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.dependence.StaticLibResolveDependence import StaticLibResolveDependence

from wudoo.SystemWillExecutor import SystemWillExecutor

DEPENT_MODULE_PATH_STORRAGE = {}

Project = CompileCPPProject

def DefaultCPPCompilation(project, objRoot = None, binDestFSItem = None):
	compilation = CPPCompilation(project, objRoot = objRoot, binDestFSItem = binDestFSItem) 
	compilation.setCompiler(GPPCompiler())
	return compilation

def nopSetupCompilation(compilation):
	pass

def getCompilationGoalPath(compilation):
	return compilation.getGoalFSItem().getPathNameExt()

def wsetupDefaultPathsFromRoot(compilation, root = None):
	if root is None:
		root = os.path.join(compilation.getProject().getRoot(), "Out")
	compilation.setObjRoot(os.path.join(root, "Obj"))
	compilation.setBinDestFSItem(os.path.join(root, "Bin", compilation.getProject().getName()))
	compilation.setDependenceBuildRoot(os.path.join(root, "Outer"))
	
def wdefaultBuild(
		project, 
		setupCompilationCallback = nopSetupCompilation, 
		willExecutor = SystemWillExecutor()
		):
	compilation = DefaultCPPCompilation(project)
	setupCompilationCallback(compilation)
	compilation.compile(willExecutor)
	compilation.resolveDependings(willExecutor)
	compilation.buildBinary(willExecutor)
#	writeCompilation(compilation)
#	compilation.setGoal(settings.getGoal())
#	compilation.setOutputDir(settings.getOutputDir())
#	compilation.setObjDir(settings.getObjDir())
#	compilation.setBinDir(settings.getBinDir())
	
#def writeCompilation(compilation):
#	pass

def moduleFile2basePath(modFile):
	return os.path.abspath(os.path.normpath(os.path.join(modFile, "..")))

def addDependProjDir(dppdPath):
	dppdPath = os.path.normpath(dppdPath)
	if not DEPENT_MODULE_PATH_STORRAGE.has_key(dppdPath):
		DEPENT_MODULE_PATH_STORRAGE[dppdPath] = dppdPath
		sys.path.append(dppdPath)

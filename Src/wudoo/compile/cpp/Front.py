import os, sys

from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.dependence.StaticLibResolveDependence import StaticLibResolveDependence
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

DEPENT_MODULE_PATH_STORRAGE = {}

Project = CompileCPPProject

def DefaultCPPCompilation(
		project, 
#		objRoot = None, 
		binDestFSItem = None
		):
	compilation = CPPCompilation(
		project, 
#		objRoot = objRoot, 
#		binDestFSItem = binDestFSItem
		) 
	compilation.setCompiler(GPPCompiler())
	return compilation

#def getCompilationGoalPath(compilation):
#	return compilation.getGoalFSItem().getPathNameExt()

def wsetupDefaultPathsFromRoot(compilation, project, root = None):
	if root is None:
		root = os.path.join(project.getRoot(), "Out")
	allocStrat = OutputRootBasedAllocate(
		root = root,
		objFolder = "Obj",
		objExt = ".o",
		binFolder = "Bin",
		outerFolder = "Outer",
		rootProject = project
		)
	compilation.setAllocateStrategy(allocStrat)
#	compilation.setObjRoot(os.path.join(root, "Obj"))
#	compilation.setBinDestFSItem(os.path.join(root, "Bin", compilation.getProject().getName()))
#	compilation.setDependenceBuildRoot(os.path.join(root, "Outer"))
	
def wdefaultBuild(
		project, 
		setupCompilationCallback = wsetupDefaultPathsFromRoot, 
		willExecutor = SystemWillExecutor(),
		compilationResult = None
		):
	compilation = DefaultCPPCompilation(project)
	setupCompilationCallback(compilation, project)
	if compilationResult is None:
		#executableFSItem = compilation.getAllocationStrategy().allocateExecutable(compilation)
#		root = os.path.join(project.getRoot(), "Out")
#		os.path.join(root, "Bin", project.getName())
		compilationResult = ExecutableCompilationResult(
			project, 
			compilation.getAllocateStrategy().allocateExecutable(project)
			)
	compilation.buildCompilationResult(compilationResult, willExecutor)

def moduleFile2basePath(modFile):
	return os.path.abspath(os.path.normpath(os.path.join(modFile, "..")))

def addDependProjDir(dppdPath):
	dppdPath = os.path.normpath(dppdPath)
	if not DEPENT_MODULE_PATH_STORRAGE.has_key(dppdPath):
		DEPENT_MODULE_PATH_STORRAGE[dppdPath] = dppdPath
		sys.path.append(dppdPath)

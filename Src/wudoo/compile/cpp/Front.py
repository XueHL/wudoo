import os, sys

from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence
from wudoo.compile.dependence.ChainCaseDependencyResolve import ChainCaseDependencyResolve
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

DEPENT_MODULE_PATH_STORRAGE = {}

Project = CompileCPPProject

def DefaultCPPCompilation(
		project, 
		binDestFSItem = None
		):
	compilation = CPPCompilation(
		project, 
		) 
	compilation.setCompiler(GPPCompiler())
	return compilation

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
	
def wdefaultBuild(
		project, 
		setupCompilationCallback = wsetupDefaultPathsFromRoot, 
		willExecutor = SystemWillExecutor(),
		compilationResult = None
		):
	compilation = DefaultCPPCompilation(project)
	setupCompilationCallback(compilation, project)
	if compilationResult is None:
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

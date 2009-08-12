import os, sys

from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.SetupCompilationUtils import *
from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence
from wudoo.compile.dependence.ChainCaseDependencyResolve import ChainCaseDependencyResolve
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult
from wudoo.compile.cpp.profile import BuildProfiles

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

from wudoo.console import Console2obj

from wudoo.compile.cpp.libscenter import PredefinedLibs

DEPENT_MODULE_PATH_STORRAGE = {}

class DefaultArgsObj:
	def __init__(self):
		self.profile = []
		self.buildroot = [None]

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

def nopSetupCompilationCallback(compilation, project):
	pass
	
def profilesChain(compilation, project, argsObj = None):
	if argsObj is None:
		argsObj = Console2obj.consoleaArgs2obj(DefaultArgsObj())
	if not (BuildProfiles.DEFAULT_PROFILE_NAME in argsObj.profile):
		argsObj.profile = [BuildProfiles.DEFAULT_PROFILE_NAME] + argsObj.profile
	for profileName in argsObj.profile:
		BuildProfiles.applyProfile(compilation, project, profileName, argsObj)
	
def wdefaultBuild(
		project, 
		setupCompilationCallback = nopSetupCompilationCallback, 
		willExecutor = SystemWillExecutor(),
		):
	compilation = DefaultCPPCompilation(project)
	profilesChain(compilation, project)
	setupCompilationCallback(compilation, project)
	compilationResult = ExecutableCompilationResult(
		project,
		compilation,
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

import os, sys

from wudoo.compile.cpp.CPPProject import CPPProject
from wudoo.compile.cpp.CPPCompilation import CPPCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.SetupCompilationUtils import *
from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence
from wudoo.compile.dependence.ChainCaseDependencyResolve import ChainCaseDependencyResolve
from wudoo.compile.dependence.CompileObjsResolveDependence import CompileObjsResolveDependence
from wudoo.compile.cpp.ExecutableCompilationResult import ExecutableCompilationResult
from wudoo.compile.cpp.profile import BuildProfiles

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.compile.libscenter.LibsRegOffice import LibsRegOffice
from wudoo.compile.ModulesRegOffice import ModulesRegOffice
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

from wudoo.console import Console2obj

from wudoo.compile.cpp.libscenter import PredefinedLibs

class DefaultArgsObj:
	def __init__(self):
		self.profile = []
		self.buildroot = [None]

Project = CPPProject

def DefaultCPPCompilation(
		binDestFSItem = None
		):
	compilation = CPPCompilation() 
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
	compilation = DefaultCPPCompilation()
	profilesChain(compilation, project)
	setupCompilationCallback(compilation, project)
	compilationResult = ExecutableCompilationResult(
		project,
		compilation,
		compilation.getAllocateStrategy().allocateExecutable(project)
		)
	compilation.buildCompilationResult(compilationResult, willExecutor)

def module2root(modulefile, upcount = 1):
	result = os.path.join(modulefile, "..")
	for i in xrange(upcount):
		result = os.path.join(result, "..")
	result = os.path.normpath(result)
	return result

LIBS_REG_OFFICE = LibsRegOffice("z:\\uaa")
MODULES_REG_OFFICE = ModulesRegOffice()
import os

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.compile.CRCSkipItemStrategy import CRCSkipItemStrategy
from wudoo.compile.cpp.SetupCompilationUtils import *

RELEASE_PROFILE_NAME = "release"
DEVELOP_PROFILE_NAME = "develop"
DEFAULT_PROFILE_NAME = "default"

BUILD_ROOT_ARGUMENT_NAME = "buildroot"

def releaseProfileExecutor(compilation, project, argsObj):
	root = argsObj.buildroot[0]
	setupPathsFromRoot(compilation, project, root)

def developProfileExecutor(compilation, project, argsObj):
	releaseProfileExecutor(compilation, project, argsObj)
	compilation.setDebugInfoLevel(100)
	compilation.setOptimisationLevel(0)
	compilation.setSkipItemsStrategy(CRCSkipItemStrategy())

EXECUTORS = {
	RELEASE_PROFILE_NAME: releaseProfileExecutor,
	DEVELOP_PROFILE_NAME: developProfileExecutor,
}
EXECUTORS[DEFAULT_PROFILE_NAME] = EXECUTORS[RELEASE_PROFILE_NAME]

def applyProfile(compilation, project, profileName, argsObj):
	profileExecutor = EXECUTORS[profileName]
	profileExecutor(compilation, project, argsObj)
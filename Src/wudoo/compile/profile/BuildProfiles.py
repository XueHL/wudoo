import os

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate
from wudoo.compile.cpp.SetupCompilationUtils import *

RELEASE_PROFILE_NAME = "release"
DEVELOP_PROFILE_NAME = "develop"
DEFAULT_PROFILE_NAME = "default"

BUILD_ROOT_ARGUMENT_NAME = "buildroot"

def releaseProfileExecutor(compilation, project, argsObj):
	root = None
	root = argsObj.buildroot[0]
	setupPathsFromRoot(compilation, project, root)

EXECUTORS = {
	RELEASE_PROFILE_NAME: releaseProfileExecutor
}
EXECUTORS[DEFAULT_PROFILE_NAME] = EXECUTORS[RELEASE_PROFILE_NAME]
EXECUTORS[DEVELOP_PROFILE_NAME] = EXECUTORS[RELEASE_PROFILE_NAME]

def applyProfile(compilation, project, profileName, argsObj):
	profileExecutor = EXECUTORS[profileName]
	profileExecutor(compilation, project, argsObj)
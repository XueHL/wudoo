import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "User-1__0-s--1-s", moduleFile = __file__)

MDL_FILE = moduleFile2basePath(__file__)
project.setRoot("..", MDL_FILE)
project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
addDependProjDir(os.path.join(MDL_FILE, "..", "..", "Lib0", "CM"))
import build_library_0
theLibPrj = build_library_0.getProject()
project.addDependenceProject(theLibPrj)

addDependProjDir(os.path.join(MDL_FILE, "..", "..", "Lib1", "CM"))
import build_library_1
theLibPrj = build_library_1.getProject()
project.addDependenceProject(theLibPrj)
### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	import os
	project = getProject()

	def setupSettCallback(compilation, project):
		setupPathsFromRoot(compilation, project)
		compilation.setResolveDependenceStrategy(StaticLibResolveDependence())

	wdefaultBuild(project, setupSettCallback)

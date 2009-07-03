import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "User-0__0-s--1-o", moduleFile = __file__)

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

	resStrat_0_s_1_o = ChainCaseDependencyResolve(StaticLibResolveDependence())
	def ifLib1ThenObj(project):
		if project.getName() == "Lib1":
			return CompileObjsResolveDependence()
	resStrat_0_s_1_o.addStage(ifLib1ThenObj)

	def setupSettCallback(compilation, project):
		setupPathsFromRoot(compilation, project)
		compilation.setResolveDependenceStrategy(resStrat_0_s_1_o)

	wdefaultBuild(project, setupSettCallback)

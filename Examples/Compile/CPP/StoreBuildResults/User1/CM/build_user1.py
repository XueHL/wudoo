import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("Store-User-1", __file__)

project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
addDependProjDir(os.path.join(project.getRoot(), "..", "TheLibrary", "CM"))
import build_thelibrary as thelibrary
theLibPrj = thelibrary.getProject()
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

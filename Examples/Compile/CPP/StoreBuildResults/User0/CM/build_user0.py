import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "UseExportHdr")

MDL_FILE = moduleFile2basePath(__file__)
project.setRoot("..", MDL_FILE)
project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
addDependProjDir(os.path.join(MDL_FILE, "..", "..", "TheLibrary", "CM"))
import build_thelibrary as thelibrary
theLibPrj = thelibrary.getProject()
project.addDependenceProject(StaticLibDependence(theLibPrj))

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
	def setupSettCallback(compilation):
		wsetupDefaultPathsFromRoot(compilation)
	wdefaultBuild(project, setupSettCallback)

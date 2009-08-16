import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("UseExportHdr", __file__)
project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
addDependProjDir(os.path.join(project.getRoot(), "..", "ExportHeaders", "CM"))
import build_exphdr
exportHdrPrj = build_exphdr.getProject()
project.addDependenceProject(exportHdrPrj)

### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	import os
	def setupBuildRoot(compilation, project):
		pass
		setupPathsFromRoot(compilation, project)
#		setupPathsFromRoot(compilation, project, "z:\\uaa")
	project = getProject()
	wdefaultBuild(project, setupBuildRoot)

import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("SLib-UseExportHdr", __file__, module2root(__file__, 2))

project.addSrcFolders(
"""
Src
CM/sub-missions/sub-src/slib
"""
)

project.addExportHdrFolders(
"""
CM/sub-missions/sub-src/slib
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
	project = getProject()
	def setupSettCallback(compilation, project):
		setupPathsFromRoot(compilation, project, os.path.normpath(os.path.join("Submission-out-0")))
		#setupPathsFromRoot(compilation, project, "z:\\uaa")
		compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
	wdefaultBuild(project, setupSettCallback)


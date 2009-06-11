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
addDependProjDir(os.path.join(MDL_FILE, "..", "..", "ExportHeaders", "CM"))
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
	def setupSettCallback(compilation):
		pass
		#exeFile = getCompilationGoalPath(compilation)
		#compilation.setDependenceBuildRoot(
		#	os.path.normpath(os.path.join(exeFile, "..", "..", "Outer"))
		#	)
	wdefaultBuild(project, setupSettCallback)

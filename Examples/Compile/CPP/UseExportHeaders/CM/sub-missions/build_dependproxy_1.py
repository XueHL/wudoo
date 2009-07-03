import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "UseExportHdr-dependProxy")

MDL_FILE = moduleFile2basePath(__file__)
project.setRoot(os.path.join("..", ".."), MDL_FILE)
project.addSrcFolders(
"""
#Src
CM/sub-missions/sub-src/proxy
"""
)

### ### Dependings  ### ###
import build_useexphdr_asstatlib_0 as build_useexphdr_asstatlib
statLibPrj = build_useexphdr_asstatlib.getProject()
project.addDependenceProject(statLibPrj)

#addDependProjDir(os.path.join(MDL_FILE, "..", "..", "..", "ExportHeaders", "CM"))
#import build_exphdr
#exportHdrPrj = build_exphdr.getProject()
#project.addDependenceProject(exportHdrPrj)

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
		setupPathsFromRoot(compilation, project, os.path.normpath(os.path.join("Submission-out-1")))
		#setupPathsFromRoot(compilation, project, "z:\\uaa")
		compilation.setResolveDependenceStrategy(StaticLibResolveDependence())	
	wdefaultBuild(project, setupSettCallback)

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
import build_useexphdr_asstatlib
statLibPrj = build_useexphdr_asstatlib.getProject()
project.addDependenceProject(StaticLibDependency(statLibPrj))

addDependProjDir(os.path.join(MDL_FILE, "..", "..", "..", "ExportHeaders", "CM"))
import build_exphdr
exportHdrPrj = build_exphdr.getProject()
project.addDependenceProject(StaticLibDependency(exportHdrPrj))

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
	settings = DefaultBuildSettings()
	settings.setDependenceBuildRoot(os.path.join(MDL_FILE, "..", "..", "Outer", "Obj"))
	wdefaultBuild(project, settings)

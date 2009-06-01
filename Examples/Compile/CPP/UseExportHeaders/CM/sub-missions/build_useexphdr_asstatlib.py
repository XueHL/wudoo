import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "UseExportHdr")

MDL_FILE = moduleFile2basePath(__file__)
project.setRoot(os.path.join("..", ".."), MDL_FILE)
project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
addDependProjDir(os.path.join(MDL_FILE, "..", "..", "..", "ExportHeaders", "CM"))
import build_exphdr
exportHdrPrj = build_exphdr.getProject()
project.addDependenceProject(exportHdrPrj, linkType = LinkTypes.STATIC_LIB)

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

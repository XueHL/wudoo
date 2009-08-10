import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "BoostUse")

project.setRoot("..", moduleFile2basePath(__file__))
project.addSrcFolders(
"""
Src
"""
)

project.addHdrFolders(
"""
Hdr
"""
)

### ### Dependings  ### ###
project.addDependenceProject(PredefinedLibs.BOOST.HEADERS_LIB)

### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	project = getProject()
	wdefaultBuild(project)

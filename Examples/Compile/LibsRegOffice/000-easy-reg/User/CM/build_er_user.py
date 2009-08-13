import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "EasyRegisterUser")

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
project.addDependenceProject(LibsRegOffice.libByName("EasyRegisterLibrary"))

### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	wdefaultBuild(project)

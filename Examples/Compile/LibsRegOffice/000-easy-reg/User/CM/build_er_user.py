import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("EasyRegisterUser", __file__)

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
project.addDependenceProject(LIBS_REG_OFFICE.libByName("EasyRegisterLibrary"))

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

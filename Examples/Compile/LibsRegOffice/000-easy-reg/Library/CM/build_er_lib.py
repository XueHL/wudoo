import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("EasyRegisterLibrary", __file__)

project.addSrcFolders(
"""
Src
"""
)

project.addExportHdrFolders(
"""
Hdr
"""
)

### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project

### ### ### Registering ### ### ### ### 
if (__name__ == "__main__"):
	print "Registering library: ", getProject().getName(), " ..."
	LIBS_REG_OFFICE.registerLibrary(getProject)
	LIBS_REG_OFFICE.flush()
	print "Completed"

import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "EasyRegisterLibrary")

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

### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project


### ### ### Registering ### ### ### ### 
if (__name__ == "__main__"):
	print "Registering library: ", getProject().getName(), " ..."
	LibsRegOffice.registerLibrary(getProject)
	print "Completed"

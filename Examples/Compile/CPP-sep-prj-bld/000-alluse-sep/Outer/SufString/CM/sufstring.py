import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("SufString", __file__)

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


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	print "Library: " + getProject().getName()

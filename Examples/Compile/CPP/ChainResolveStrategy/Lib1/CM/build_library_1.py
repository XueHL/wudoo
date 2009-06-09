import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "Lib1", moduleFile = __file__)

MDL_FILE = moduleFile2basePath(__file__)
project.setRoot("..", MDL_FILE)
project.addSrcFolders(
"""
Src
"""
)

project.addExportHdrFolders(
"""
ExportHdr
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
	print "No executable: static library only."

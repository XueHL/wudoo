import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("ExportHdr", __file__)

project.addSrcFolders(
"""
Src
SrcMain
"""
)

project.addHdrFolders(
"""
Hdr
"""
)

project.addExportHdrFolders(
"""
ExportHrd
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
	import os
	project = getProject()
	wdefaultBuild(project)

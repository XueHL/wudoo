import pickle
from wudoo.compile.cpp.Front import *
from wudoo.FSItem import FSItem

project = Project(name = "BuildEasy")

project.setRoot(os.path.join("..", ".."), moduleFile2basePath(__file__))
project.addSrcFolders(
"""
Src
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
	objRoot = os.path.normpath(os.path.join(__file__, "..", "Ched-Out"))
	binDestFSItem = FSItem(os.path.join(__file__, "..", "Ched-Out"), "ched-bin.exe")
	compilation = DefaultCPPCompilation(project, objRoot = objRoot, binDestFSItem = binDestFSItem)
	compilation.compile(SystemWillExecutor())


import pickle
from wudoo.compile.cpp.Front import *

MDL_FILE = moduleFile2basePath(__file__)

project = Project(name = "BuildEasy")

project.setRoot(os.path.join("..", ".."), MDL_FILE)
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
	def setupSettCallback(compilation):
		compilation.setObjRoot(os.path.join("Ched-Out", "Obj"))
		compilation.setGoalFSItem(os.path.join("Ched-Out", "Bin", "ched-bin.exe"))
	wdefaultBuild(project, setupSettCallback)

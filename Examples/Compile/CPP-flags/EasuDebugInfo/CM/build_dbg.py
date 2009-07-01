import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "BuildEasy")

project.setRoot("..", moduleFile2basePath(__file__))
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
	def setupSettCallback(compilation, project):
		wsetupDefaultPathsFromRoot(compilation, project)
		#compilation.setDebugInfoLevel(100)
	project = getProject()
	wdefaultBuild(project)

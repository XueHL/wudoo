import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("EasyOpt", __file__)

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
		setupPathsFromRoot(compilation, project)
		compilation.setOptimisationLevel(0)
	project = getProject()
	wdefaultBuild(project, setupSettCallback)

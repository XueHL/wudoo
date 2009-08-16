import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("BuildEasy", __file__)

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
	import tempfile
	tmpDir = tempfile.mkdtemp()
	print tmpDir
	import os
	project = getProject()
	def setupSettCallback(compilation, project):
		setupPathsFromRoot(compilation, project, os.path.normpath(os.path.join(tmpDir, "Ched-Out")))
	wdefaultBuild(project, setupSettCallback)

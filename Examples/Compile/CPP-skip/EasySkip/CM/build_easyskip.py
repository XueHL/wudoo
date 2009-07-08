import pickle
from wudoo.compile.cpp.Front import *

project = Project(name = "EasySkip")

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


### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	project = getProject()
	def setupSettCallback(compilation, project):
		argsObj = DefaultArgsObj()
		argsObj.profile = ["develop"]
		profilesChain(compilation, project, argsObj)
	wdefaultBuild(project, setupSettCallback)
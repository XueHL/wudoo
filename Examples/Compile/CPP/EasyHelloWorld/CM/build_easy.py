import pickle
from wudoo.compile.cpp.Front import *

project = Project()

project.setRoot("..")
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

if (__name__ == "__main__"):
	settings = DefaultBuildSettings()
	project = getProject()
	settings.outputDir = project.getRoot() + "/" + "Out"
	settings.outputBinName = "HelloWorld.exe"
	WDefaultBuild(project, settings)

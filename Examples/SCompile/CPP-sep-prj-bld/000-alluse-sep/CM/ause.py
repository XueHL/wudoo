import pickle
from wudoo.compile.cpp.Front import *

project = CPPProject("AUSe", __file__)

project.addSrcFolders(
"""
Src
"""
)

### ### Dependings  ### ###
project.addDependenceProject(projectByName("SufString"))
project.addDependenceProject(PredefinedLibs.BOOST.BOOST_COMMON_LIB)


### ### ### ### ### ### ### ### ### ### 
storrage = pickle.dumps(project)
del project

def getProject():
	project = pickle.loads(storrage)
	return project

### ### ### ### ### ### ### ### ### ### 
if (__name__ == "__main__"):
	print "Program: " + getProject().getName()

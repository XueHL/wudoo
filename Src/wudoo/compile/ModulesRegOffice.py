import sys, os

class ModulesRegOffice:
	def __init__(self):
		self.__modulesPathStorrage = set(sys.path)
	
	def addDependProjDir(self, dppdPath):
		dppdPath = os.path.normpath(dppdPath)
		if not dppdPath in self.__modulesPathStorrage:
			self.__modulesPathStorrage.add(dppdPath)
			sys.path.append(dppdPath)

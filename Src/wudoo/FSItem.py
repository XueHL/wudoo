import os

class FSItem:
	def __init__(self, *pathSteps):
		self.__pathSteps = [st for st in pathSteps]
	
	def getPathNameExt(self, start = 0):
		return os.path.join(*self.__pathSteps[start:])
	
	def getPath(self, start = 0):
		if len(self.__pathSteps) <= 1:
			return ""
		return os.path.join(*self.__pathSteps[start:-1])
	
	def getPathArr(self, start = 0):
		return self.__pathSteps[start:-1]
	
	def getBegOfPath(self, count = -1):
		if count == -1: count = len(self.__pathSteps) - 1
		return os.path.join(*self.__pathSteps[:count])
	
	def getNameExt(self):
		n = len(self.__pathSteps)
		return self.__pathSteps[n - 1]
	
	def getExt(self):
		return os.path.splitext(self.getNameExt())[1][1:]
	
	def getName(self):
		return os.path.splitext(self.getNameExt())[0]
		
	def __str__(self):
		return self.getPathNameExt();
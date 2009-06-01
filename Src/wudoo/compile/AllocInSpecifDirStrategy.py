import os
from wudoo.compile.IAllocObjStrategy import IAllocObjStrategy
from wudoo.FSItem import FSItem

class AllocInSpecifDirStrategy(IAllocObjStrategy):
	def __init__(self, root, resultExtension):
		self.__root = root
		self.__resultExtension = resultExtension
		
	def allocate(self, fsItem):
		path = [self.__root]
		path.extend(fsItem.getPathArr(1)) 
		path.append(fsItem.getName() + self.__resultExtension)
		return FSItem(*path)

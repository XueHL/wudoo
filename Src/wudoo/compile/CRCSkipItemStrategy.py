import os
from wudoo.FSItem import FSItem
from wudoo.compile.ISkipItemsStrategy import ISkipItemsStrategy

class CRCSkipItemStrategy(ISkipItemsStrategy):
	def __init__(self, objExt = ".skipcrc"):
		self.__objExt = objExt

	def skip(self, srcFsItem, objFsItem):
		crcFSItem = self.__getCRCFile(objFsItem)
		if not os.path.exists(crcFSItem.getPathNameExt()):
			return False
		bufCmpld = open(crcFSItem.getPathNameExt(), "r").read()
		bufSrc = open(srcFsItem.getPathNameExt(), "r").read()
		return bufSrc == bufCmpld

	def onCompiled(self, srcFsItem, objFsItem):
		buf = open(srcFsItem.getPathNameExt(), "r").read()
		crcFSItem = self.__getCRCFile(objFsItem)
		f = open(crcFSItem.getPathNameExt(), "w")
		f.write(buf)
		f.close()

	def __getCRCFile(self, objFSItem):
		path = objFSItem.getPathArr()
		path.append(objFSItem.getName() + self.__objExt)
		return FSItem(*path)
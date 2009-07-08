import os
import pickle
from wudoo.FSItem import FSItem
from wudoo.compile.buildresult.skipcompile.ISkipItemsStrategy import ISkipItemsStrategy

class CRCSkipItemStrategy(ISkipItemsStrategy):
	def __init__(self, objExt = ".skipcrc"):
		self.__objExt = objExt

	def skip(self, srcFsItem, compilation, project):
		crcFSItem = compilation.getAllocateStrategy().allocateSingleProjInfo(project, self.__objExt)
		if not os.path.exists(crcFSItem.getPathNameExt()):
			return False
		crcStorr = open(crcFSItem.getPathNameExt(), "r").read()
		crcStorr = pickle.loads(crcStorr)
		if not crcStorr.has_key(srcFsItem.getPathNameExt()):
			return False
		bufCmpld = crcStorr[srcFsItem.getPathNameExt()]
		bufSrc = open(srcFsItem.getPathNameExt(), "r").read()
		return bufSrc == bufCmpld

	def onCompiled(self, srcFsItem, compilation, project):
		crcFSItem = compilation.getAllocateStrategy().allocateSingleProjInfo(project, self.__objExt)
		if os.path.exists(crcFSItem.getPathNameExt()):
			crcStorr = open(crcFSItem.getPathNameExt(), "r").read()
			crcStorr = pickle.loads(crcStorr)
		else:
			crcStorr = {}
		buf = open(srcFsItem.getPathNameExt(), "r").read()
		crcStorr[srcFsItem.getPathNameExt()] = buf
		f = open(crcFSItem.getPathNameExt(), "w")
		crcStorr = pickle.dumps(crcStorr)
		f.write(crcStorr)
		f.close()

	def __getCRCFile(self, objFSItem):
		path = objFSItem.getPathArr()
		path.append(objFSItem.getName() + self.__objExt)
		return FSItem(*path)
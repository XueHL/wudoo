import os
import pickle
from wudoo.FSItem import FSItem
from wudoo.compile.buildresult.skipcompile.ISkipItemsStrategy import ISkipItemsStrategy
from wudoo.fsrecutils import CPPDependUtils
from wudoo.compile import SourceFilterColl

class CRCSkipItemStrategy(ISkipItemsStrategy):
	HEADER_FILTER = None

	def __init__(self, objExt = ".skipcrc"):
		self.__objExt = objExt
		self.__projects = set()
		self.__header2allIncludedList = {}
		self.__headers = set()

	def skip(self, srcFsItem, compilation, project):
		self.__addProjectHeaders(project)
		checkItems = self.__getCheckList(srcFsItem)
		#print "\n\n\t", srcFsItem, ":\n", "", [ci.__str__() for ci in checkItems]
		return self.__checkItemsCRC(checkItems, compilation)

	def onCompiled(self, srcFsItem, compilation, project):
		crcFSItem = compilation.getAllocateStrategy().allocateSingleCompileInfo(self.__objExt)
		if os.path.exists(crcFSItem.getPathNameExt()):
			crcStorr = open(crcFSItem.getPathNameExt(), "r").read()
			crcStorr = pickle.loads(crcStorr)
		else:
			crcStorr = {}
		storeItems = self.__getCheckList(srcFsItem)
		del srcFsItem
		for item in storeItems:
			buf = open(item.getPathNameExt(), "r").read()
			crcStorr[item.getPathNameExt()] = buf
		f = open(crcFSItem.getPathNameExt(), "w")
		crcStorr = pickle.dumps(crcStorr)
		f.write(crcStorr)
		f.close()

	def __getCRCFile(self, objFSItem):
		path = objFSItem.getPathArr()
		path.append(objFSItem.getName() + self.__objExt)
		return FSItem(*path)

	def __addProjectHeaders(self, project):
		allNewHdrFolders = []
		for depPrj in CPPDependUtils.getAllDependProjects(project, True):
			if depPrj in self.__projects:
				continue
			self.__projects.add(depPrj)
			CPPDependUtils.appendHeaderFolders(depPrj.getExportHdrFolders(), depPrj, allNewHdrFolders)
			CPPDependUtils.appendHeaderFolders(depPrj.getHdrFolders(), depPrj, allNewHdrFolders)
		allHeaderItems = CPPDependUtils.getFilteredFiles([], allNewHdrFolders, SourceFilterColl.HDR_SOURCE_FILTER)
		self.__registerHeaders(allHeaderItems)

	def __registerHeaders(self, headersFSItemsList):
		self.__headers.update(headersFSItemsList)
		for headerFSIt in headersFSItemsList:
			self.__buildDepends4header(headerFSIt)

	def __buildDepends4header(self, hfsi):
		dependset = set()
		lastdepend = set([hfsi])
		#print "bdp: ", hfsi
		while len(lastdepend) > 0:
			newlastdepend = []
			for dep in lastdepend:
				buf = open(dep.getPathNameExt(), "r").read()
				for cand in self.__headers:
					name = cand.getNameExt()
					if buf.find(name) == -1:
						continue
					#print "cand: ", name, " - accepted"
					if not (cand in dependset):
						dependset.add(cand)
						if self.__header2allIncludedList.has_key(cand):
							dependset.update(self.__header2allIncludedList[cand])
						else:
							newlastdepend.append(cand)
			lastdepend = newlastdepend
		self.__header2allIncludedList[hfsi] = dependset


	def __getIncludedList(self, fsItem):
		if self.__includedItems.has_key(fsItem):
			return self.__includedItems[fsItem]
		else:
			inclList = []
			self.__includedItems[fsItem] = inclList
			return inclList

	def __getCheckList(self, srcFsItem):
		buf = open(srcFsItem.getPathNameExt(), "r").read()
		result = set([srcFsItem])
		for hdr in self.__headers:
			name = hdr.getNameExt()
			if buf.find(name) > -1:
				result.add(hdr)
				result.update(self.__header2allIncludedList[hdr])
		return result			

	def __checkItemsCRC(self, checkItemsList, compilation):
		crcFSItem = compilation.getAllocateStrategy().allocateSingleCompileInfo(self.__objExt)
		if not os.path.exists(crcFSItem.getPathNameExt()):
			return False
		crcStorr = open(crcFSItem.getPathNameExt(), "r").read()
		crcStorr = pickle.loads(crcStorr)
		for item in checkItemsList:
			if not crcStorr.has_key(item.getPathNameExt()):
				return False
			bufCmpld = crcStorr[item.getPathNameExt()]
			bufSrc = open(item.getPathNameExt(), "r").read()
			if bufSrc != bufCmpld:
				return False
		return True

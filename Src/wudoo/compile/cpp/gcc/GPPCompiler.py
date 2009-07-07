import os
from wudoo.compile.BaseCompiler import BaseCompiler
from wudoo.compile.CreateDestOnPreCompile import CreateDestOnPreCompile

class GPPCompiler(BaseCompiler):
	GPP_COMPILER_CMD = "g++"
	GPP_ARCHIVE_CMD = "ar"

	def __init__(self, preCompileStrategy = CreateDestOnPreCompile()):
		BaseCompiler.__init__(self)
		self.__gppCmd = GPPCompiler.GPP_COMPILER_CMD
		self.__arCmd = GPPCompiler.GPP_ARCHIVE_CMD
		self.__preCompileStrategy = preCompileStrategy

	def compile(self, srcFSItem, objFSItem, project, compilation, willExecutor):
		command = self.__gppCmd + \
			" -c " + \
			'"' + srcFSItem.getPathNameExt() + '"' + \
			" -o " + \
			'"' + objFSItem.getPathNameExt() + '"' + \
			self.__buildHdrString(project) + \
			" " + self.__getFlags(compilation) + \
			""
		self.__preCompileStrategy.onPreCompile(objFSItem)
		willExecutor.execute(command)
	
	def linkExecutable(self, objectFSItems, goalFSItem, willExecutor):
		objStr = ""
		for obj in objectFSItems:
			objStr += " \"" + obj.getPathNameExt() + '"'
		command = self.__gppCmd + \
			objStr + \
			" -o " + \
			'"' + goalFSItem.getPathNameExt() + '"' + \
			""
		self.__preCompileStrategy.onPreLink(goalFSItem)
		willExecutor.execute(command)

	def archive(self, project, compilation, willExecutor, goalFSItem):
		objStr = ""
		for obj in compilation.getObjectFSItems():
			objStr += " \"" + obj.getPathNameExt() + '"'
		command = self.__arCmd + \
			" q " + \
			'"' + goalFSItem.getPathNameExt() + '"' + \
			objStr + \
			""
		self.__preCompileStrategy.onPreLink(goalFSItem)
		willExecutor.execute(command)

	def __buildHdrString(self, project):
		allhdrs = []
		self.__addHdrFolders(project.getHdrFolders(), project, allhdrs)
		self.__dfsAddExportHderFromDependences(project, allhdrs)
		result = " "
		for hdr in allhdrs:
			result += ' -I"' + hdr + '"'
		return result

	def __dfsAddExportHderFromDependences(self, project, allhdrs):
		self.__addHdrFolders(project.getExportHdrFolders(), project, allhdrs)
		for depPrj in project.getDependences():
			self.__dfsAddExportHderFromDependences(depPrj, allhdrs)

	def __addHdrFolders(self, folderList, project, dest):
		for hdr in folderList:
			dest.append(os.path.join(project.getRoot(), hdr))

	def __getFlags(self, compilation):
		return self.__getDebugInfoFlags(compilation) + " " + \
			self.__getOptimisationFlags(compilation) + \
			""

	def __getDebugInfoFlags(self, compilation):
		debugInfoLevel = compilation.getDebugInfoLevel()
		debugInfoLevel = self.__reduce2range(debugInfoLevel, 0, 3)
		return "-g" + str(debugInfoLevel)

	def __getOptimisationFlags(self, compilation):
		optimisationLevel = compilation.getOptimisationLevel()
		optimisationLevel = self.__reduce2range(optimisationLevel, 0, 3)
		return "-O" + str(optimisationLevel)

	def __reduce2range(self, debugInfoLevel, beg, end):
		rnge = end - beg
		rnge *= debugInfoLevel / 100.0
		rnge = int(rnge)
		assert(rnge >= beg and rnge <= end)
		return rnge + beg

import unittest, os.path, sys, tempfile

from wudoo.compile.Project import Project
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.FSItem import FSItem

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

class TestCompiler(unittest.TestCase):
	def getSrc2ObjMap(self):
		return self.__map
	def getProject(self):
		return self
	def getHdrFolders(self):
		return []
	def getExportHdrFolders(self):
		return []
	def getDependences(self):
		return []

	def testProjectRootPathSet(self):
		we = StoreCallsWillExecutor()
		compiler = GPPCompiler()
		srcItem = FSItem("C:/Work/Src/main.cpp");
		objItem = FSItem("C:/Work/Out/Obj/main.o");
		self.__map = { srcItem: objItem }
		compiler.compile(srcItem, self, we)
		self.assertEquals(["g++ -c \"C:/Work/Src/main.cpp\" -o \"C:/Work/Out/Obj/main.o\" "], we.history)

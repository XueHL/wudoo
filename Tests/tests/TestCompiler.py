import unittest, os.path, sys, tempfile
from wudoo.compile.Project import Project
from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler

class TestCompiler(unittest.TestCase):
	def testProjectRootPathSet(self):
		we = StoreCallsWillExecutor()
		Compiler = GPPCompiler(willExecutor = we)
		Compiler.compile("Src/main.cpp", "Out/Obj/main.o")
		self.assertEquals(["g++ -c Src/main.cpp -o Out/Obj/main.o"], we.history)

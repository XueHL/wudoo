import unittest, os.path, sys, tempfile
from wudoo.compile.Project import Project
from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor
from wudoo.compile.cpp.gcc.GPPCompilator import GPPCompilator

class TestCompilator(unittest.TestCase):
	def testProjectRootPathSet(self):
		we = StoreCallsWillExecutor()
		compilator = GPPCompilator(willExecutor = we)
		compilator.compile("Src/main.cpp", "Out/Obj/main.o")
		self.assertEquals(["g++ -c Src/main.cpp -o Out/Obj/main.o"], we.history)

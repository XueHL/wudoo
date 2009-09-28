import unittest, sys, os, tempfile, subprocess

from wudoo.compile.cpp.Front import *
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool

class TestBoost(unittest.TestCase):
	def setUp(self):
		sys.path.append(
			os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP-predefined-libs", "Boost", "CM"))
		)
		import build_boost_use
		TestBoost.boostPrj = build_boost_use.getProject()
		tmpDir = tempfile.mktemp()
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool.data")
		TestBoost.getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF

	def tearDown(self):
		n = len(sys.path)
		del sys.path[n - 1]
		del TestBoost.boostPrj
		StoreCompilationPool._StoreCompilationPool__getPoolFile = TestBoost.getPoolFile

	def testSharedPtr(self):
		tmpDir = tempfile.mktemp()
		def setupCompilationCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(TestBoost.boostPrj, setupCompilationCallback)
		executable = None
		for sf in os.listdir(os.path.join(tmpDir, "Bin")):
			if os.path.splitext(sf)[0] == "BoostUse":
				executable = sf
		self.assertFalse(executable is None)
		executable = os.path.join(tmpDir, "Bin", executable)
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("shared_ptr created: 0 shared_ptr destroyed: 0\r\nshared_ptr created: 22 shared_ptr destroyed: 22\r\n", result)

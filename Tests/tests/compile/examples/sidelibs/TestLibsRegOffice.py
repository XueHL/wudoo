import unittest, sys, os, tempfile, subprocess

from wudoo.compile.cpp.Front import *
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool

class TestLibsRegOffice(unittest.TestCase):
	def setUp(self):
		sys.path.append(
			os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "000-easy-reg", "Library", "CM"))
		)
		sys.path.append(
			os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "000-easy-reg", "User", "CM"))
		)
		import build_er_lib
		import build_er_user
		TestLibsRegOffice.userProj = build_er_user.getProject()
		tmpDir = tempfile.mktemp()
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool.data")
		TestLibsRegOffice.getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF

	def tearDown(self):
		n = len(sys.path)
		del sys.path[n - 1]
		del sys.path[n - 2]
		del TestLibsRegOffice.userProj
		StoreCompilationPool._StoreCompilationPool__getPoolFile = TestLibsRegOffice.getPoolFile

	def testLibRegOffile(self):
		tmpDir = tempfile.mktemp()
		def setupCompilationCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(TestLibsRegOffice.userProj, setupCompilationCallback)
		executable = None
		for sf in os.listdir(os.path.join(tmpDir, "Bin")):
			if os.path.splitext(sf)[0] == "EasyRegisterUser":
				executable = sf
		executable = os.path.join(tmpDir, "Bin", executable)
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("easy-reg :: Library\r\n", result)
		
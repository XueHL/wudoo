import unittest, sys, os, tempfile, subprocess

from wudoo.compile.cpp.Front import *
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool
from wudoo.IWillReportHandler import *

class TestLibsRegOffice(unittest.TestCase):
	def setUp(self):
		sys.path.append(
			os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "000-easy-reg", "User", "CM"))
		)
		build_er_lib_cmd = os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "000-easy-reg", "Library", "CM", "build_er_lib.py"))
		build_er_lib_cmd = "python " + build_er_lib_cmd
		SystemWillExecutor(NOPWillReportHandler()).execute(build_er_lib_cmd)
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

class TestLocalLibsSearch(unittest.TestCase):
	def setUp(self):
		globalLibCmd = os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "001-glob-loc", "GlobalLib", "CM", "build_glb_lib.py"))
		globalLibCmd = "python " + globalLibCmd
		SystemWillExecutor(NOPWillReportHandler()).execute(globalLibCmd)
		sys.path.append(
			os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "LibsRegOffice", "001-glob-loc", "User", "CM"))
		)
		import build_GL_user
		TestLocalLibsSearch.userProj = build_GL_user.getProject()
		tmpDir = tempfile.mktemp()
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool.data")
		TestLocalLibsSearch.getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF

	def tearDown(self):
		n = len(sys.path)
		del sys.path[n - 1]
		del TestLocalLibsSearch.userProj
		StoreCompilationPool._StoreCompilationPool__getPoolFile = TestLocalLibsSearch.getPoolFile

	def testDevelopingProjectsSearch(self):
		tmpDir = tempfile.mktemp()
		def setupCompilationCallback(compilation, project):
			argsObj = DefaultArgsObj()
			argsObj.developprojects = ["LocalLibrary"]
			argsObj.developprojectssearch = [".."]
			profilesChain(compilation, project, argsObj)
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(TestLocalLibsSearch.userProj, setupCompilationCallback)
		executable = None
		for sf in os.listdir(os.path.join(tmpDir, "Bin")):
			if os.path.splitext(sf)[0] == "GLUser":
				executable = sf
		executable = os.path.join(tmpDir, "Bin", executable)
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("The Global\r\nThe Local\r\n", result)
		
import unittest, os, sys, tempfile

from wudoo.SystemWillExecutor import SystemWillExecutor

from wudoo.compile.cpp.CPPProject import CPPProject
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter
from wudoo.compile.compilationpool.StoreCompilationPool import StoreCompilationPool
from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

def ifLib1ThenObj(project):
	from wudoo.compile.cpp.Front import CompileObjsResolveDependence
	if project.getName() == "Lib1":
		return CompileObjsResolveDependence()

class TestStoringCompilation(unittest.TestCase):
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "StoreBuildResults", "User0", "CM"))					
		)
	import build_user0 as usr0prj
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "StoreBuildResults", "User1", "CM"))					
		)
	import build_user1 as usr1prj
	
	def testTheLibraryExample(self):
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild
		tmpDir = tempfile.mktemp()
		tmp0 = os.path.join(tmpDir, "p0") 
		tmp1 = os.path.join(tmpDir, "p1")
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool.data")
		getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF
		 
		usr0prj = TestStoringCompilation.usr0prj.getProject()
		def setupTmpdirCallback0(compilation, project):
			setupPathsFromRoot(compilation, project, tmp0)
			compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(usr0prj, setupTmpdirCallback0, scwe)
		trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User0\\Src\\main.cpp" -o "__TMP__\\p0\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr" -g0 -O3', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\Src\\NameHolder.cpp" -o "__TMP__\\p0\\Outer\\TheLibrary\\Src\\NameHolder.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr" -g0 -O3', 
			'ar q "__TMP__\\p0\\Outer\\TheLibrary.a" "__TMP__\\p0\\Outer\\TheLibrary\\Src\\NameHolder.o"', 
			'g++ "__TMP__\\p0\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\TheLibrary.a" -o "__TMP__\\p0\\Bin\\Store-User-0"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj2346", tmp0, tmp0)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\Store-User-0.exe', 
			'Obj\\Src\\main.o', 
			'Outer\\TheLibrary.a', 
			'Outer\\TheLibrary\\Src\\NameHolder.o'
			], 
			objPaths
			)
		
		usr1prj = TestStoringCompilation.usr1prj.getProject()
		def setupTmpdirCallback1(compilation, project):
			setupPathsFromRoot(compilation, project, tmp1)
			compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(usr1prj, setupTmpdirCallback1, scwe)
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User1\\Src\\main.cpp" -o "__TMP__\\p1\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr" -g0 -O3', 
			'g++ "__TMP__\\p1\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\TheLibrary.a" -o "__TMP__\\p1\\Bin\\Store-User-1"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj", tmp1, tmp1)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\Store-User-1.exe', 
			'Obj\\Src\\main.o', 
			], 
			objPaths
			)

		StoreCompilationPool._StoreCompilationPool__getPoolFile = getPoolFile

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "ChainResolveStrategy", "User-0__0-s--1-o", "CM"))
		)
	import build_chain_0 as chain0prj
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "ChainResolveStrategy", "User-1__0-s--1-s", "CM"))
		)
	import build_chain_1 as chain1prj

	def testChainResolve_so_ss(self):
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild, ChainCaseDependencyResolve, CompileObjsResolveDependence
		tmpDir = tempfile.mktemp()
		tmp0 = os.path.join(tmpDir, "p0") 
		tmp1 = os.path.join(tmpDir, "p1")
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool_" + project.getName() + ".data")
		getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF
		 
		chain0prj = TestStoringCompilation.chain0prj.getProject()
		def setupTmpdirCallback0(compilation, project):
			setupPathsFromRoot(compilation, project, tmp0)
			#compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
			resStrat_0_s_1_o = ChainCaseDependencyResolve(StaticLibResolveDependence())
			resStrat_0_s_1_o.addStage(ifLib1ThenObj)
			compilation.setResolveDependenceStrategy(resStrat_0_s_1_o)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(chain0prj, setupTmpdirCallback0, scwe)
		trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\User-0__0-s--1-o\\Src\\main.cpp" -o "__TMP__\\p0\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib0\\ExportHdr" -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\ExportHdr" -g0 -O3', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib0\\Src\\NameHolder0.cpp" -o "__TMP__\\p0\\Outer\\Lib0\\Src\\NameHolder0.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib0\\ExportHdr" -g0 -O3', 
			'ar q "__TMP__\\p0\\Outer\\Lib0.a" "__TMP__\\p0\\Outer\\Lib0\\Src\\NameHolder0.o"', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\Src\\NameHolder1.cpp" -o "__TMP__\\p0\\Outer\\Lib1\\Src\\NameHolder1.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\ExportHdr" -g0 -O3', 
			'g++ "__TMP__\\p0\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\Lib0.a" "__TMP__\\p0\\Outer\\Lib1\\Src\\NameHolder1.o" -o "__TMP__\\p0\\Bin\\User-0__0-s--1-o"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("PrjFindSources", tmp0, tmp0)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\User-0__0-s--1-o.exe', 
			'Obj\\Src\\main.o', 
			'Outer\\Lib0.a', 
			'Outer\\Lib0\\Src\\NameHolder0.o', 
			'Outer\\Lib1\\Src\\NameHolder1.o'
			], 
			objPaths
			)
		
		chain1prj = TestStoringCompilation.chain1prj.getProject()
		def setupTmpdirCallback1(compilation, project):
			setupPathsFromRoot(compilation, project, tmp1)
			compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(chain1prj, setupTmpdirCallback1, scwe)
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\User-1__0-s--1-s\\Src\\main.cpp" -o "__TMP__\\p1\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib0\\ExportHdr" -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\ExportHdr" -g0 -O3', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\Src\\NameHolder1.cpp" -o "__TMP__\\p1\\Outer\\Lib1\\Src\\NameHolder1.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\ChainResolveStrategy\\Lib1\\ExportHdr" -g0 -O3', 
			'ar q "__TMP__\\p1\\Outer\\Lib1.a" "__TMP__\\p1\\Outer\\Lib1\\Src\\NameHolder1.o"', 
			'g++ "__TMP__\\p1\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\Lib0.a" "__TMP__\\p1\\Outer\\Lib1.a" -o "__TMP__\\p1\\Bin\\User-1__0-s--1-s"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj", tmp1, tmp1)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\User-1__0-s--1-s.exe',
			'Obj\\Src\\main.o',
			'Outer\\Lib1.a',
			'Outer\\Lib1\\Src\\NameHolder1.o',
			], 
			objPaths
			)

		StoreCompilationPool._StoreCompilationPool__getPoolFile = getPoolFile

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP-flags", "EasyDebugInfo", "CM"))
		)
	import build_dbg as dbgprj

	def testDbgInfo(self):
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild, ChainCaseDependencyResolve, CompileObjsResolveDependence
		tmpDir = tempfile.mktemp()
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool_" + project.getName() + ".data")
		getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF
		 
		dbginfoprj = TestStoringCompilation.dbgprj.getProject()
		def setupTmpdirCallback0(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
			compilation.setDebugInfoLevel(100)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(dbginfoprj, setupTmpdirCallback0, scwe)
		trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP-flags\\EasyDebugInfo\\Src\\Hello.cpp" -o "__TMP__\\Obj\\Src\\Hello.o"  -g3 -O3', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP-flags\\EasyDebugInfo\\Src\\Main.cpp" -o "__TMP__\\Obj\\Src\\Main.o"  -g3 -O3', 
			'g++ "__TMP__\\Obj\\Src\\Hello.o" "__TMP__\\Obj\\Src\\Main.o" -o "__TMP__\\Bin\\EasyDbg"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj", tmpDir, tmpDir)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\EasyDbg.exe', 
			'Obj\\Src\\Hello.o', 
			'Obj\\Src\\Main.o',
			], 
			objPaths
			)
		
		hellobuf = open(os.path.join(tmpDir, objPaths[1]), "r").read()
		self.assertTrue(hellobuf.find("CPP-flags") > 0)

		### no debuginfo

		tmpDir = tempfile.mktemp()
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool_" + project.getName() + ".data")
		getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF
		 
		dbginfoprj = TestStoringCompilation.dbgprj.getProject()
		def setupTmpdirCallback0(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
			#compilation.setDebugInfoLevel(100)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(dbginfoprj, setupTmpdirCallback0, scwe)
		trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP-flags\\EasyDebugInfo\\Src\\Hello.cpp" -o "__TMP__\\Obj\\Src\\Hello.o"  -g0 -O3', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP-flags\\EasyDebugInfo\\Src\\Main.cpp" -o "__TMP__\\Obj\\Src\\Main.o"  -g0 -O3', 
			'g++ "__TMP__\\Obj\\Src\\Hello.o" "__TMP__\\Obj\\Src\\Main.o" -o "__TMP__\\Bin\\EasyDbg"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj", tmpDir, tmpDir)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\EasyDbg.exe', 
			'Obj\\Src\\Hello.o', 
			'Obj\\Src\\Main.o',
			], 
			objPaths
			)
		
		hellobuf = open(os.path.join(tmpDir, objPaths[1]), "r").read()
		self.assertTrue(hellobuf.find("CPP-flags") < 0)

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

	def __recCP(src, dest):
		if os.path.isfile(src):
			b = open(src, "r").read()
			if not os.path.exists(os.path.split(dest)[0]):
				os.makedirs(os.path.split(dest)[0])
			f = open(dest, "w")
			f.write(b)
			f.close()
		else:
			for sub in os.listdir(src):
				TestStoringCompilation.recCP(os.path.join(src, sub), os.path.join(dest, sub))
		pass
	recCP = staticmethod(__recCP)

	def __cloneSkipTest():
		skroot = os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP-skip", "EasySkip"))
		sktemp = tempfile.mktemp()
		sys.path.append(os.path.join(sktemp, "CM"))
		TestStoringCompilation.recCP(skroot, sktemp)
		return sktemp
	cloneSkipTest = staticmethod(__cloneSkipTest)

	def testSkipStrat(self):
		skroot = TestStoringCompilation.cloneSkipTest()
		import build_easyskip as skipprj
		from wudoo.console import Console2obj
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild, ChainCaseDependencyResolve, CompileObjsResolveDependence, profilesChain
		tmpDir = tempfile.mktemp()
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationPool_" + project.getName() + ".data")
		getPoolFile = StoreCompilationPool._StoreCompilationPool__getPoolFile
		StoreCompilationPool._StoreCompilationPool__getPoolFile = faikGPF
		 
		skipinfoprj = skipprj.getProject()

		class DefaultArgsObj: pass
		argsObj = Console2obj.argArr2obj(("--profile develop --buildroot " + tmpDir).split(" "), DefaultArgsObj())
		def setupCompilationCallback(compilation, project):
			profilesChain(compilation, project, argsObj)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(skipinfoprj, setupCompilationCallback, scwe)
		history = "@".join(scwe.history).replace(skroot, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Src\\foo-0.cpp" -o "__TMP__\\Obj\\Src\\foo-0.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ -c "__TRUNK__\\Src\\foo-1.cpp" -o "__TMP__\\Obj\\Src\\foo-1.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ -c "__TRUNK__\\Src\\main.cpp" -o "__TMP__\\Obj\\Src\\main.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ "__TMP__\\Obj\\Src\\foo-0.o" "__TMP__\\Obj\\Src\\foo-1.o" "__TMP__\\Obj\\Src\\main.o" -o "__TMP__\\Bin\\EasySkip"'
			], 
			history
			)
		del history
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe

		project = CPPProject("Prj", tmpDir, tmpDir)
		project.addSrcFolders("\n".join(os.listdir(project.getRoot())))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe", "a": "a", "skipcrc": "skipcrc"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(
			[
			'Bin\\EasySkip.exe', 'Obj\\EasySkip-info.skipcrc', 'Obj\\Src\\foo-0.o', 'Obj\\Src\\foo-1.o', 'Obj\\Src\\main.o',
			], 
			objPaths
			)
		
		## no ch
		import subprocess
		executableLoc = os.path.join(tmpDir, "Bin")

		scwe = StoreCallsWillExecutor()
		wdefaultBuild(skipinfoprj, setupCompilationCallback, scwe)
		history = "@".join(scwe.history).replace(skroot, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			#'g++ -c "__TRUNK__\\Src\\foo-0.cpp" -o "__TMP__\\Obj\\Src\\foo-0.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			#'g++ -c "__TRUNK__\\Src\\foo-1.cpp" -o "__TMP__\\Obj\\Src\\foo-1.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			#'g++ -c "__TRUNK__\\Src\\main.cpp" -o "__TMP__\\Obj\\Src\\main.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ "__TMP__\\Obj\\Src\\foo-0.o" "__TMP__\\Obj\\Src\\foo-1.o" "__TMP__\\Obj\\Src\\main.o" -o "__TMP__\\Bin\\EasySkip"'
			], 
			history
			)
                swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe
		executable = None
		for sf in os.listdir(executableLoc):
			if os.path.splitext(sf)[0] == "EasySkip":
				executable = sf
		self.assertFalse(executable is None)
		executable = os.path.join(executableLoc, executable)
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("Foo-0\r\nFoo-1", result)

		## with ch cpp

		chpth = os.path.join(skroot, "Src", "foo-1.cpp")
		b = open(chpth, "r").read().replace("THE_RESULT", "THE_RESULT_CH")
		f = open(chpth, "w")
		f.write(b)
		f.close()
			
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(skipinfoprj, setupCompilationCallback, scwe)
		#trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(skroot, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			#'g++ -c "__TRUNK__\\Src\\foo-0.cpp" -o "__TMP__\\Obj\\Src\\foo-0.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ -c "__TRUNK__\\Src\\foo-1.cpp" -o "__TMP__\\Obj\\Src\\foo-1.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			#'g++ -c "__TRUNK__\\Src\\main.cpp" -o "__TMP__\\Obj\\Src\\main.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ "__TMP__\\Obj\\Src\\foo-0.o" "__TMP__\\Obj\\Src\\foo-1.o" "__TMP__\\Obj\\Src\\main.o" -o "__TMP__\\Bin\\EasySkip"'
			], 
			history
			)
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("Foo-0\r\nFoo-1 - ch", result)

		## with ch hdr

		chpth = os.path.join(skroot, "Hdr", "results.h")
		b = open(chpth, "r").read().replace('"Foo-1 - ch"', '"Foo-1 - ch - hdr"')
		f = open(chpth, "w")
		f.write(b)
		f.close()
			
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(skipinfoprj, setupCompilationCallback, scwe)
		#trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(skroot, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			#'g++ -c "__TRUNK__\\Src\\foo-0.cpp" -o "__TMP__\\Obj\\Src\\foo-0.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ -c "__TRUNK__\\Src\\foo-1.cpp" -o "__TMP__\\Obj\\Src\\foo-1.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			#'g++ -c "__TRUNK__\\Src\\main.cpp" -o "__TMP__\\Obj\\Src\\main.o"  -I"__TRUNK__\\Hdr" -g3 -O0', 
			'g++ "__TMP__\\Obj\\Src\\foo-0.o" "__TMP__\\Obj\\Src\\foo-1.o" "__TMP__\\Obj\\Src\\main.o" -o "__TMP__\\Bin\\EasySkip"'
			], 
			history
			)
		swe = SystemWillExecutor()
		for cmd in scwe.history:
			swe.execute(cmd)
		del scwe
		result = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
		self.assertEqual("Foo-0\r\nFoo-1 - ch - hdr", result)
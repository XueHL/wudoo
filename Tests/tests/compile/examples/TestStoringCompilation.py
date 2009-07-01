import unittest, os, sys, tempfile

from wudoo.SystemWillExecutor import SystemWillExecutor

from wudoo.compile.Project import Project
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter
from wudoo.compile.compilationpool.StoreCompilationaPool import StoreCompilationaPool
from wudoo.compile.dependence.StaticLibResolveDependence import StaticLibResolveDependence

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

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
		from wudoo.compile.cpp.Front import wsetupDefaultPathsFromRoot, wdefaultBuild
		tmpDir = tempfile.mktemp()
		tmp0 = os.path.join(tmpDir, "p0") 
		tmp1 = os.path.join(tmpDir, "p1")
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationaPool.data")
		getPoolFile = StoreCompilationaPool._StoreCompilationaPool__getPoolFile
		StoreCompilationaPool._StoreCompilationaPool__getPoolFile = faikGPF
		 
		usr0prj = TestStoringCompilation.usr0prj.getProject()
		def setupTmpdirCallback0(compilation, project):
			wsetupDefaultPathsFromRoot(compilation, project, tmp0)
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

		project = Project(tmp0)
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
			wsetupDefaultPathsFromRoot(compilation, project, tmp1)
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

		project = Project(tmp1)
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

		StoreCompilationaPool._StoreCompilationaPool__getPoolFile = getPoolFile

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
		from wudoo.compile.cpp.Front import wsetupDefaultPathsFromRoot, wdefaultBuild, ChainCaseDependencyResolve, CompileObjsResolveDependence
		tmpDir = tempfile.mktemp()
		tmp0 = os.path.join(tmpDir, "p0") 
		tmp1 = os.path.join(tmpDir, "p1")
		
		def faikGPF(self, project):
			return os.path.join(tmpDir, "StoreCompilationaPool_" + project.getName() + ".data")
		getPoolFile = StoreCompilationaPool._StoreCompilationaPool__getPoolFile
		StoreCompilationaPool._StoreCompilationaPool__getPoolFile = faikGPF
		 
		chain0prj = TestStoringCompilation.chain0prj.getProject()
		def setupTmpdirCallback0(compilation, project):
			wsetupDefaultPathsFromRoot(compilation, project, tmp0)
			#compilation.setResolveDependenceStrategy(StaticLibResolveDependence())
			resStrat_0_s_1_o = ChainCaseDependencyResolve(StaticLibResolveDependence())
			def ifLib1ThenObj(project):
				if project.getName() == "Lib1":
					return CompileObjsResolveDependence()
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

		project = Project(tmp0)
		print tmp0
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
			wsetupDefaultPathsFromRoot(compilation, project, tmp1)
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

		project = Project(tmp1)
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

		StoreCompilationaPool._StoreCompilationaPool__getPoolFile = getPoolFile

import unittest, os, sys, tempfile

#from wudoo.FSItem import FSItem
from wudoo.SystemWillExecutor import SystemWillExecutor

#from wudoo.compile.cpp.Front import DefaultCPPCompilation
#from wudoo.compile.BaseCompilation import BaseCompilation
#from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.compile.Project import Project
#from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter

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
		TheLibrary_compilations = os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "StoreBuildResults", "TheLibrary", "CM", "TheLibrary.compilations"))
		if os.path.exists(TheLibrary_compilations):
			os.remove(TheLibrary_compilations)
		self.assertFalse(os.path.exists(TheLibrary_compilations))
		
		from wudoo.compile.cpp.Front import wsetupDefaultPathsFromRoot, wdefaultBuild
		tmpDir = tempfile.mktemp()
		tmp0 = os.path.join(tmpDir, "p0") 
		tmp1 = os.path.join(tmpDir, "p1")
		 
		usr0prj = TestStoringCompilation.usr0prj.getProject()
		def setupTmpdirCallback0(compilation):
			wsetupDefaultPathsFromRoot(compilation, tmp0)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(usr0prj, setupTmpdirCallback0, scwe)
		trunk = os.path.normpath(os.path.join(sys.path[0], "..")) 
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User0\\Src\\main.cpp" -o "__TMP__\\p0\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\Src\\NameHolder.cpp" -o "__TMP__\\p0\\Outer\\TheLibrary\\Src\\NameHolder.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
			'ar q "__TMP__\\p0\\Outer\\TheLibrary.a" "__TMP__\\p0\\Outer\\TheLibrary\\Src\\NameHolder.o"', 
			'g++ "__TMP__\\p0\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\TheLibrary.a" -o "__TMP__\\p0\\Bin\\UseExportHdr"'
#			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User0\\Src\\main.cpp" -o "__TMP__\\p0\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
#			'g++ "__TMP__\\p0\\Obj\\Src\\main.o" "z:\\temp\\tmpxuvri_\\p1\\Outer\\TheLibrary.a" -o "__TMP__\\p0\\Bin\\UseExportHdr"'
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
			'Bin\\UseExportHdr.exe', 
			'Obj\\Src\\main.o', 
			'Outer\\TheLibrary.a', 
			'Outer\\TheLibrary\\Src\\NameHolder.o'
			], 
			objPaths
			)
		
		usr1prj = TestStoringCompilation.usr1prj.getProject()
		def setupTmpdirCallback1(compilation):
			wsetupDefaultPathsFromRoot(compilation, tmp1)
		scwe = StoreCallsWillExecutor()
		wdefaultBuild(usr1prj, setupTmpdirCallback1, scwe)
		history = "@".join(scwe.history).replace(trunk, "__TRUNK__").replace(tmpDir, "__TMP__").split("@")
		self.assertEqual(
			[
#			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User1\\Src\\main.cpp" -o "__TMP__\\p1\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
#			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\Src\\NameHolder.cpp" -o "__TMP__\\p1\\Outer\\TheLibrary\\Src\\NameHolder.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
#			'ar q "__TMP__\\p1\\Outer\\TheLibrary.a" "__TMP__\\p1\\Outer\\TheLibrary\\Src\\NameHolder.o"', 
#			'g++ "__TMP__\\p1\\Obj\\Src\\main.o" "__TMP__\\p1\\Outer\\TheLibrary.a" -o "__TMP__\\p1\\Bin\\UseExportHdr"'
			'g++ -c "__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\User1\\Src\\main.cpp" -o "__TMP__\\p1\\Obj\\Src\\main.o"  -I"__TRUNK__\\Examples\\Compile\\CPP\\StoreBuildResults\\TheLibrary\\ExportHdr"', 
			'g++ "__TMP__\\p1\\Obj\\Src\\main.o" "__TMP__\\p0\\Outer\\TheLibrary.a" -o "__TMP__\\p1\\Bin\\UseExportHdr"'
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
			'Bin\\UseExportHdr.exe', 
			'Obj\\Src\\main.o', 
#			'Outer\\TheLibrary.a', 
#			'Outer\\TheLibrary\\Src\\NameHolder.o'
			], 
			objPaths
			)

		if os.path.exists(TheLibrary_compilations):
			os.remove(TheLibrary_compilations)
		self.assertFalse(os.path.exists(TheLibrary_compilations))

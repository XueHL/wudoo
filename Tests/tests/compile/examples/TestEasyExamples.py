import unittest, os, sys, tempfile

from wudoo.FSItem import FSItem
from wudoo.SystemWillExecutor import SystemWillExecutor

from wudoo.compile.cpp.Front import DefaultCPPCompilation
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.Project import Project
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

class TestEasyExamples(unittest.TestCase):
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "UseExportHeaders", "CM"))					
		)
	import build_useexphdr as build_useexphdr_prj
	
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "UseExportHeaders", "CM", "sub-missions"))					
		)
	import build_dependproxy_1 as build_dependproxy_prj
	
	def testCompile(self):
		from tests.compile.TestCompilation import TestCompilation
		project = TestCompilation.build_easy_prj.getProject()
		compilation = BaseCompilation(project)
#		compilation.setGoalFSItem(FSItem("C:\Work", "hello.exe"))
		tmpDir = tempfile.mkdtemp()
#		strat = AllocInSpecifDirStrategy(tmpDir, ".o")
#		compilation.setAllocateObjStrategy(strat)
#		compilation.setCompiler(GPPCompiler())
		we = StoreCallsWillExecutor()
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild
		def setupCompilationCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(project, setupCompilationCallback, we)
#		compilation.compile(we)
#		compilation.resolveDependings(we)
#		compilation.buildBinary(we)
		we.history.sort()
		cmd = we.history[2]
		self.assertTrue(cmd.find("g++") > -1)
		self.assertTrue(cmd.find("-c") > -1)
		self.assertTrue(cmd.find("Main.cpp") > -1)
		self.assertTrue(cmd.find("-o") > -1)
		self.assertTrue(cmd.find("Main.o") > -1)
		cmd = we.history[0]
		self.assertTrue(cmd.find("g++") > -1)
		self.assertTrue(cmd.find("Hello.o") > -1)
		self.assertTrue(cmd.find("Main.o") > -1)
		
	def testEasyBuildReal(self):
		from tests.compile.TestCompilation import TestCompilation
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild
		project = TestCompilation.build_easy_prj.getProject()
#		compilation = DefaultCPPCompilation(project)
		tmpDir = tempfile.mkdtemp()
#		strat = AllocInSpecifDirStrategy(tmpDir, ".o")
#		compilation.setAllocateObjStrategy(strat)
		def setupCompilationCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(project, setupCompilationCallback)
#		compilation.buildWorkFlow(SystemWillExecutor())
		project = Project(tmpDir)
		project.addSrcFolders("\n".join(os.listdir(tmpDir)))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(["Bin\\BuildEasy.exe", "Obj\\Src\\Hello.o", "Obj\\Src\\Main.o"], objPaths)
		
	def testBuildDepend(self):
		project = TestEasyExamples.build_useexphdr_prj.getProject()
#		compilation = DefaultCPPCompilation(project)
		tmpDir = tempfile.mkdtemp()
		from wudoo.compile.cpp.Front import setupPathsFromRoot, wdefaultBuild
		def setupCompilationCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(project, setupCompilationCallback)
#		compilation.setGoalFSItem(FSItem(tmpDir, "Bin", project.getName() + ".exe"));
#		compilation.setObjRoot(os.path.join(tmpDir, "Obj"))
#		compilation.setDependenceBuildRoot(os.path.join(tmpDir, "Outer", "Obj"))
#		compilation.buildWorkFlow(SystemWillExecutor())
		project = Project(tmpDir)
		project.addSrcFolders("\n".join(os.listdir(tmpDir)))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(["Bin\\UseExportHdr.exe", "Obj\\Src\\main.o", "Outer\\ExportHdr\\SrcMain\\main.o", "Outer\\ExportHdr\\Src\\ExportHello.o"], objPaths)

	def testProxyStatlibEquilibristic(self):
		project = TestEasyExamples.build_dependproxy_prj.getProject()
		project.findSources()
		tmpDir = tempfile.mkdtemp()
		from wudoo.compile.cpp.Front import wdefaultBuild, setupPathsFromRoot  
		def setupTmpdirCallback(compilation, project):
			setupPathsFromRoot(compilation, project, tmpDir)
		wdefaultBuild(project, setupTmpdirCallback)
	
		project = Project(tmpDir)
		project.addSrcFolders("\n".join(os.listdir(tmpDir)))
		project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe"}));
		project.findSources()
		objItems = project.getSourceItems()
		objPaths = [io.getPathNameExt(1) for io in objItems]
		objPaths.sort()
		self.assertEquals(["Bin\\UseExportHdr-dependProxy.exe", "Obj\\CM\\sub-missions\\sub-src\\proxy\\main.o", "Outer\\ExportHdr\\SrcMain\\main.o", "Outer\\ExportHdr\\Src\\ExportHello.o", "Outer\\SLib-UseExportHdr\\CM\\sub-missions\\sub-src\\slib\\foo.o", "Outer\\SLib-UseExportHdr\\Src\\main.o"], 
			objPaths
			)


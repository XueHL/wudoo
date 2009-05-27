import unittest, os, sys, tempfile

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.Front import DefaultCPPCompilation
from wudoo.compile.Project import Project
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

class TestCompilation(unittest.TestCase):
    additp = sys.path[0]
    additp = os.path.join(additp, "..", "Examples", "Compile", "CPP", "EasyHelloWorld", "CM")
    additp = os.path.normpath(additp)
    sys.path.append(additp)
    import build_easy
    build_easy_prj = build_easy
    
    def testTrivialCompilation(self):
        project = TestCompilation.build_easy_prj.getProject()
        compilation = BaseCompilation(project)
        self.assertTrue(isinstance(compilation, ICompilation))
        self.assertEquals(project, compilation.getProject())
    
    def testAllocObjStrategy(self):
        project = TestCompilation.build_easy_prj.getProject()
        compilation = BaseCompilation(project)
        tmpDir = tempfile.mkdtemp()
        strat = AllocInSpecifDirStrategy(tmpDir, ".o")
        compilation.setAllocateObjStrategy(strat)
        ex = None
        try:
            compilation.compile(StoreCallsWillExecutor())
        except Exception, e:
            ex = e
        self.assertTrue(ex is not None)
        src2obj = compilation.getSrc2ObjMap()
        srcs = project.getSourceItems()
        src = srcs[0]
        if src.getName() != "Main":
            src = srcs[1]
        self.assertEquals("Main", src.getName())
        obj = src2obj[src]
        self.assertEquals(os.path.join("Src", "Main.o"), obj.getPathNameExt(1))
        
    def testCompile(self):
        project = TestCompilation.build_easy_prj.getProject()
        compilation = BaseCompilation(project)
        compilation.setGoalFSItem(FSItem("C:\Work", "hello.exe"))
        tmpDir = tempfile.mkdtemp()
        strat = AllocInSpecifDirStrategy(tmpDir, ".o")
        compilation.setAllocateObjStrategy(strat)
        compilation.setCompiler(GPPCompiler())
        we = StoreCallsWillExecutor()
        compilation.compile(we)
        we.history.sort()
        cmd = we.history[1]
        self.assertTrue(cmd.find("g++") > -1)
        self.assertTrue(cmd.find("-c") > -1)
        self.assertTrue(cmd.find("Main.cpp") > -1)
        self.assertTrue(cmd.find("-o") > -1)
        self.assertTrue(cmd.find("Main.o") > -1)
        cmd = we.history[2]
        self.assertTrue(cmd.find("g++") > -1)
        self.assertTrue(cmd.find("Hello.o") > -1)
        self.assertTrue(cmd.find("Main.o") > -1)
        self.assertTrue(cmd.find("-o C:\Work\hello.exe") > -1)
        
    def testEasyBuildReal(self):
        project = TestCompilation.build_easy_prj.getProject()
        compilation = DefaultCPPCompilation(project)
        tmpDir = tempfile.mkdtemp()
        compilation.setGoalFSItem(FSItem(tmpDir, "Bin", project.getName() + ".exe"));
        strat = AllocInSpecifDirStrategy(tmpDir, ".o")
        compilation.setAllocateObjStrategy(strat)
        compilation.compile(SystemWillExecutor())
        project = Project(tmpDir)
        srcFolder = TestCompilation.build_easy_prj.getProject().getSrcFolders()[0] 
        project.addSrcFolders(srcFolder)
        project.addSrcFolders("Bin")
        project.setSourceFilter(ExtensionBasedFilter({"o": "o", "exe": "exe"}));
        project.findSources()
        objItems = project.getSourceItems()
        objPaths = [io.getPathNameExt(1) for io in objItems]
        objPaths.sort()
        self.assertEquals(["Bin\\BuildEasy.exe", "Src\\Hello.o", "Src\\Main.o"], objPaths)
        
        
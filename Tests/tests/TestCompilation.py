import unittest, os, sys, tempfile

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy

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
            compilation.compile()
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
        return
        project = TestCompilation.build_easy_prj.getProject()
        compilation = BaseCompilation(project)
        tmpDir = tempfile.mkdtemp()
        strat = AllocInSpecifDirStrategy(tmpDir, ".o")
        compilation.setAllocateObjStrategy(strat)
        compilation.setCompiler()
        compilation.compile()
        
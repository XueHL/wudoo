import unittest, os, sys, tempfile

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.cpp.gcc.GPPCompiler import GPPCompiler
from wudoo.compile.cpp.Front import DefaultCPPCompilation
from wudoo.compile.Project import Project
from wudoo.filter.ExtensionBasedFilter import ExtensionBasedFilter
from wudoo.SystemWillExecutor import SystemWillExecutor
from wudoo.FSItem import FSItem

from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

class TestCompilation(unittest.TestCase):
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "EasyHelloWorld", "CM"))					
		)
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
		
		
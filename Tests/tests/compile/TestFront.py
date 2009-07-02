import unittest, os, sys, tempfile

from wudoo.compile.cpp.Front import *

class TestCompilation(unittest.TestCase):
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "UseExportHeaders", "CM"))					
		)
	import build_useexphdr as build_useexphdr_prj

	def testFillCompilationWithProfile(self):
		from wudoo.console import Console2obj
		project = TestCompilation.build_useexphdr_prj.getProject()
		compilation = DefaultCPPCompilation(project)
		argsObj = Console2obj.argArr2obj("--profile develop".split(" "))
		profilesChain(compilation, project, argsObj)
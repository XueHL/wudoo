import unittest, os, sys, tempfile

from wudoo.compile.cpp.Front import *
from tests.fakes.StoreCallsWillExecutor import StoreCallsWillExecutor

class TestFront(unittest.TestCase):
	sys.path.append(
		os.path.normpath(os.path.join(sys.path[0], "..", "Examples", "Compile", "CPP", "UseExportHeaders", "CM"))					
		)
	import build_useexphdr as build_useexphdr_prj

	def testFillDevelopCompilation(self):
		from wudoo.console import Console2obj
		project = TestFront.build_useexphdr_prj.getProject()
		compilation = DefaultCPPCompilation(project)
		import tempfile
		tmpDir = tempfile.mkdtemp()
		argsObj = Console2obj.argArr2obj(("--profile develop --buildroot " + tmpDir).split(" "), DefaultArgsObj())
		willExecutor = StoreCallsWillExecutor()
		def setupCompilationCallback(compilation, project):
			profilesChain(compilation, project, argsObj)
		wdefaultBuild(project, setupCompilationCallback, willExecutor)
		history = willExecutor.history
		history = "@@@".join(history).replace(tmpDir, "__WS__").split("@@@")
		src = os.path.normpath(os.path.join(project.getModuleFile(), "..", "..", ".."))
		history = "@@@".join(history).replace(src, "__SRC__").split("@@@")
		
		self.assertEquals(
			[
			'g++ -c "__SRC__\\UseExportHeaders\\Src\\main.cpp" -o "__WS__\\Obj\\Src\\main.o"  -I"__SRC__\\ExportHeaders\\ExportHrd" -g3 -O0', 
			'g++ -c "__SRC__\\ExportHeaders\\Src\\ExportHello.cpp" -o "__WS__\\Outer\\ExportHdr\\Src\\ExportHello.o"  -I"__SRC__\\ExportHeaders\\Hdr" -I"__SRC__\\ExportHeaders\\ExportHrd" -g3 -O0', 
			'g++ -c "__SRC__\\ExportHeaders\\SrcMain\\main.cpp" -o "__WS__\\Outer\\ExportHdr\\SrcMain\\main.o"  -I"__SRC__\\ExportHeaders\\Hdr" -I"__SRC__\\ExportHeaders\\ExportHrd" -g3 -O0',
			'g++ "__WS__\\Obj\\Src\\main.o" "__WS__\\Outer\\ExportHdr\\Src\\ExportHello.o" -o "__WS__\\Bin\\UseExportHdr"'
			],
			history
			)
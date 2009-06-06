import unittest, os.path, sys
from wudoo.compile.Project import Project
from wudoo.compile import SourceFilterColl
from wudoo.compile.cpp.CompileCPPProject import CompileCPPProject 

class TestProject(unittest.TestCase):
	def testCPPSearch(self):
		project = CompileCPPProject()
		project.setRoot(os.path.join("..", "Examples", "Compile", "CPP", "EasyHelloWorld"))
		project.addSrcFolders("Src")
		project.findSources()
		srcItems = project.getSourceItems()
		srcItems = [fsi.getPathNameExt(1) for fsi in srcItems]
		srcItems.sort()
		self.assertEquals(["Src\\Hello.cpp", "Src\\Main.cpp"], srcItems)
		
	def testProjectRootPathSet(self):
		project = Project()
		project.setRoot("tests/pam/param/..")
		root = project.getRoot()
		self.assertEquals(-1, root.find(".."))
		self.assertTrue(root.find("pam") > 0)

	def testProjectItems(self):
		project = Project()
		project.setSourceFilter(SourceFilterColl.ACCEPT_ALL_FILTER)
		project.setRoot("tests/pam/param/../../../..")
		project.addSrcFolders("Tests")
		self.assertEqual([], project.getSourceItems())
		project.findSources()
		self.assertTrue(len(project.getSourceItems()) > 3)
		
	def testAddSourceFolder2Project(self):
		project = Project()
		project.addSrcFolders(
"""
Src
Hdr
"""
			)
		self.assertEquals(["Src", "Hdr"], project.getSrcFolders())

		
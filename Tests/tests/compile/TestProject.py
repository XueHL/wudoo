import unittest, os.path, sys
from wudoo.compile.cpp.CPPProject import CPPProject
from wudoo.compile import SourceFilterColl
from wudoo.compile.cpp.CPPProject import CPPProject 

class TestProject(unittest.TestCase):
	def testCPPSearch(self):
		project = CPPProject("Pr123", "NoAddress", os.path.join("..", "Examples", "Compile", "CPP", "EasyHelloWorld"))
		project.addSrcFolders("Src")
		project.findSources()
		srcItems = project.getSourceItems()
		srcItems = [fsi.getPathNameExt(1) for fsi in srcItems]
		srcItems.sort()
		self.assertEquals(["Src\\Hello.cpp", "Src\\Main.cpp"], srcItems)
		
	def testProjectRootPathSet(self):
		project = CPPProject("Prj", "NA", "tests/pam/param/..")
		root = project.getRoot()
		self.assertEquals(-1, root.find(".."))
		self.assertTrue(root.find("pam") > 0)

	def testProjectItems(self):
		project = CPPProject("Prj", "NoAddress", "tests/pam/param/../../../..")
		project.setSourceFilter(SourceFilterColl.ACCEPT_ALL_FILTER)
		project.addSrcFolders("Tests")
		self.assertEqual([], project.getSourceItems())
		project.findSources()
		self.assertTrue(len(project.getSourceItems()) > 3)
		
	def testAddSourceFolder2Project(self):
		project = CPPProject("Prj5674", "NoAddress", "NoAddress")
		project.addSrcFolders(
"""
Src
Hdr
"""
			)
		self.assertEquals(["Src", "Hdr"], project.getSrcFolders())

		
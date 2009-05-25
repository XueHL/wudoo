import unittest, os.path, sys
from wudoo.compile.Project import Project
from wudoo.compile import SourceFilterColl 

class TestProject(unittest.TestCase):
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
		
		 
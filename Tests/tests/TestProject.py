import unittest, os.path, sys
from wudoo.compile.Project import Project

class TestProject(unittest.TestCase):
	def testProjectRootPathSet(self):
		project = Project()
		project.setRoot("tests/pam/param/..")
		root = project.getRoot()
		self.assertEquals(-1, root.find(".."))
		self.assertTrue(root.find("pam") > 0)

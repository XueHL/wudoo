import unittest

from wudoo.console import Console2obj

class TestConsole2Obj(unittest.TestCase):
	def testOneVal(self):
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"ignore", "it",
			"--field0", "v0"
			]
			)
		self.assertEquals(["v0"], consInfo.field0)

	def testMultiVal(self):
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"ignore", "it",
			"--field0", "v0",
			"--field1", "v0", "v1", "v2",
			"--field2", "v0", "v1", "v2",
			]
			)
		self.assertEquals(
			{
			"field2": ["v0", "v1", "v2"], 
			"field1": ["v0", "v1", "v2"],
			"field0": ["v0"], 
			}
			, consInfo.__dict__
			)

	def testSysArgv(self):
		consInfo = Console2obj.consoleaArgs2obj()
		self.assertEquals({}, consInfo.__dict__)
	
	def testDefaults(self):
		class Defl: pass
		obj = Defl()
		obj.setField = ["v0"]
		obj.setBoolField = True
		obj.resetBoolField = False
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"--setField", "v1", "v2",
			"-b-resetBoolField", "True",
			"-b-notsetBoolField", "True"
			],
			obj,
			)
		self.assertEquals(
			{
			"setField": ["v1", "v2"], 
			"setBoolField": True, 
			"resetBoolField": True, 
			"notsetBoolField": True,
			}
			, consInfo.__dict__
			)

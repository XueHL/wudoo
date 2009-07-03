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
	
	def testDefaultEmptyList(self):
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"--setField", "v0", "v1"
			],
			"notSetField0",
			"notSetField1",
			"setField",
			)
		self.assertEquals(
			{
			"setField": ["v0", "v1"], 
			"notSetField0": [],
			"notSetField1": [],
			}
			, consInfo.__dict__
			)

	def testKWDefaultBool(self):
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"--setField", "v0", "v1"
			],
			"notSetField0",
			boolField = True,
			)
		self.assertEquals(
			{
			"setField": ["v0", "v1"], 
			"notSetField0": [],
			"boolField": True,
			}
			, consInfo.__dict__
			)

	def testBool(self):
		consInfo = Console2obj.argArr2obj(
			[
			"python",
			"TestConsole2Obj.py",
			"--setField", "v0", "v1",
			"-b-boolField", "True",
			]
			)
		self.assertEquals(
			{
			"setField": ["v0", "v1"], 
			"boolField": True,
			}
			, consInfo.__dict__
			)

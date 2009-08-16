import sys, os.path, unittest

testPackagePath = sys.path[0]
trunkPath = os.path.join(testPackagePath, "..")
trunkPath = os.path.normpath(trunkPath)
srcRoot = os.path.join(trunkPath, "Src")
sys.path.append(srcRoot)
sys.path.append(os.path.join(trunkPath, "Tests"))

import tests.compile.TestProject
import tests.compile.TestItemsWork
import tests.compile.TestCompilation
import tests.compile.TestCompiler
import tests.compile.examples.TestEasyExamples
import tests.compile.examples.TestStoringCompilation
import tests.console.TestConsole2Obj
import tests.compile.TestFront
import tests.compile.examples.sidelibs.TestBoost
import tests.compile.examples.sidelibs.TestLibsRegOffice

testsuit = unittest.TestSuite([\
	unittest.TestLoader().loadTestsFromModule(tests.compile.TestProject),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.TestItemsWork),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.TestCompilation),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.TestCompiler),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.TestEasyExamples),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.TestStoringCompilation),\
	unittest.TestLoader().loadTestsFromModule(tests.console.TestConsole2Obj),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.TestFront),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.sidelibs.TestBoost),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.sidelibs.TestLibsRegOffice),\
	])
unittest.TextTestRunner(verbosity=2).run(testsuit)

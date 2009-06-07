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

testsuit = unittest.TestSuite([\
#	unittest.TestLoader().loadTestsFromModule(tests.compile.TestProject),\
#	unittest.TestLoader().loadTestsFromModule(tests.compile.TestItemsWork),\
#	unittest.TestLoader().loadTestsFromModule(tests.compile.TestCompilation),\
#	unittest.TestLoader().loadTestsFromModule(tests.compile.TestCompiler),\
#	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.TestEasyExamples),\
	unittest.TestLoader().loadTestsFromModule(tests.compile.examples.TestStoringCompilation),\
	])
unittest.TextTestRunner(verbosity=2).run(testsuit)

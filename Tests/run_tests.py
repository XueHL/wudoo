import sys, os.path, unittest

testPackagePath = sys.path[0]
trunkPath = os.path.join(testPackagePath, "..")
trunkPath = os.path.normpath(trunkPath)
srcRoot = os.path.join(trunkPath, "Src")
sys.path.append(srcRoot)
sys.path.append(os.path.join(trunkPath, "Tests"))

import tests.TestProject
import tests.TestCompilator

testsuit = unittest.TestSuite([\
	unittest.TestLoader().loadTestsFromModule(tests.TestProject),\
	unittest.TestLoader().loadTestsFromModule(tests.TestCompilator),\
        ])
unittest.TextTestRunner(verbosity=2).run(testsuit)

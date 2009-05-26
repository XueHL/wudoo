import unittest, os, sys

from wudoo.compile.ICompilation import ICompilation
from wudoo.compile.BaseCompilation import BaseCompilation

class TestCompilation(unittest.TestCase):
    def testTrivialCompilation(self):
        additp = sys.path[0]
        additp = os.path.join(additp, "..", "Examples", "Compile", "CPP", "EasyHelloWorld", "CM")
        additp = os.path.normpath(additp)
        sys.path.append(additp)
        import build_easy
        project = build_easy.getProject()
        compilation = BaseCompilation(project)
        self.assertTrue(isinstance(compilation, ICompilation))
        self.assertEquals(project, compilation.getProject())

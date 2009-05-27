import os
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy

class CPPCompilation(BaseCompilation):
    def __init__(self, project, objRoot = None):
        BaseCompilation.__init__(self, project)
        if objRoot is None:
            objRoot = os.path.join(project.getRoot(), "Out", "Obj")
        self.setAllocateObjStrategy(
            AllocInSpecifDirStrategy(objRoot, "o")
            )
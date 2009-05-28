import os
from wudoo.compile.BaseCompilation import BaseCompilation
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy
from wudoo.FSItem import FSItem

class CPPCompilation(BaseCompilation):
    def __init__(self, project, objRoot = None, binDestFSItem = None):
        BaseCompilation.__init__(self, project)
        if objRoot is None:
            objRoot = os.path.join(project.getRoot(), "Out", "Obj")
        if binDestFSItem is None:
            binDestFSItem = FSItem(project.getRoot(), os.path.join("Out", "Bin"), project.getName())
        self.setAllocateObjStrategy(
            AllocInSpecifDirStrategy(objRoot, "o")
            )
        self.setGoalFSItem(binDestFSItem)
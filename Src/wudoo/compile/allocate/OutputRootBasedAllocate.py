import os

from wudoo.compile.allocate.IAllocateStrategy import IAllocateStrategy
from wudoo.compile.AllocInSpecifDirStrategy import AllocInSpecifDirStrategy

class OutputRootBasedAllocate(IAllocateStrategy):
    def __init__(
            self,
            root,
            binFolder,
            outerFolder,
            objFolder = None,
            objExt = None,
            allocObjectsStrategy = None,
            ):
        self.__root = root
        self.__objFolder = objFolder
        self.__binFolder = binFolder
        self.__outerFolder = outerFolder
        if allocObjectsStrategy is None:
            allocObjectsStrategy = AllocInSpecifDirStrategy(os.path.join(root, objFolder), objExt)
        self.__allocObjectsStrategy = allocObjectsStrategy
        
    def allocateObj(self, src):
        return self.__allocObjectsStrategy.allocate(src)
        
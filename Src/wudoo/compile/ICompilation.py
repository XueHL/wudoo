class ICompilation:
    def compile(self):
        raise NotImplementedError()

    def getProject(self):
        raise NotImplementedError()

    def setAllocateObjStrategy(self, strat):
        raise NotImplementedError()

    def getSrc2ObjMap(self):
        raise NotImplementedError()
    
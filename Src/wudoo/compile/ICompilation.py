class ICompilation:
    def compile(self, willExecutor):
        raise NotImplementedError()

    def getProject(self):
        raise NotImplementedError()

    def setAllocateObjStrategy(self, strat):
        raise NotImplementedError()

    def getSrc2ObjMap(self):
        raise NotImplementedError()

    def setCompiler(self, compiler):
        raise NotImplementedError()
    
    def setObjRoot(self, objRoot):
        raise NotImplementedError()
    
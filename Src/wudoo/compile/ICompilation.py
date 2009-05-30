class ICompilation:
    def buildWorkFlow(self, willExecutor):
        raise NotImplementedError()
    
    def compile(self, willExecutor):
        raise NotImplementedError()
    
    def resolveDependings(self, willExecutor):
        raise NotImplementedError()

    def buildBinary(self, willExecutor):
        raise NotImplementedError()

    def getAllObjectItems(self, **params):
        raise NotImplementedError()

    def getProject(self):
        raise NotImplementedError()

    def getSrc2ObjMap(self):
        raise NotImplementedError()

    def setCompiler(self, compiler):
        raise NotImplementedError()
    
    def setObjRoot(self, objRoot):
        raise NotImplementedError()

    def setAllocateObjStrategy(self, strat):
        raise NotImplementedError()
    
from wudoo.compile.ICompilation import ICompilation

class BaseCompilation(ICompilation):
    def __init__(self, project):
        self.__project = project
        self.__allocObjStrategy = None
        self.__src2objMap = {}
        
    def getProject(self):
        return self.__project

    def setAllocateObjStrategy(self, strat):
        self.__allocObjStrategy = strat

    def getSrc2ObjMap(self):
        return self.__src2objMap
        
    def compile(self):
        self.__project.findSources()
        for src in self.__project.getSourceItems():
            obj = self.__allocObjStrategy.allocate(src)
            self.__src2objMap[src] = obj
        compiler.compile()
        
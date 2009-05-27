from wudoo.compile.ICompilation import ICompilation

class BaseCompilation(ICompilation):
    def __init__(self, project):
        self.__project = project
        self.__goalFSItem = None
        self.__allocObjStrategy = None
        self.__src2objMap = {}
        self.__compiler = None
        
    def getProject(self):
        return self.__project

    def setAllocateObjStrategy(self, strat):
        self.__allocObjStrategy = strat

    def setGoalFSItem(self, goalFSItem):
        self.__goalFSItem = goalFSItem

    def getSrc2ObjMap(self):
        return self.__src2objMap
        
    def compile(self, willExecutor):
        self.__project.findSources()
        self.__buildObjMap()
        self.__compileObjs(willExecutor)
        self.__compileBinary(willExecutor)
        
    def __buildObjMap(self):
        for src in self.__project.getSourceItems():
            obj = self.__allocObjStrategy.allocate(src)
            self.__src2objMap[src] = obj
            
    def __compileObjs(self, willExecutor):
        for src in self.__project.getSourceItems():
            self.__compiler.compile(src, self, willExecutor)
            
    def __compileBinary(self, willExecutor):
        self.__compiler.link(self.__project, self, willExecutor, self.__goalFSItem)

    def setCompiler(self, compiler):
        self.__compiler = compiler
        
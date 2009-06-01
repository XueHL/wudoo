import os
from wudoo.compile.ICompilation import ICompilation
from wudoo.FSItem import FSItem

class BaseCompilation(ICompilation):
    def __init__(self, project):
        self.__project = project
        self.__goalFSItem = None
        self.__allocObjStrategy = None
        self.__src2objMap = {}
        self.__compiler = None
        #self.__dependenceObjects = []
        
    def getProject(self):
        return self.__project

    def getSrc2ObjMap(self):
        return self.__src2objMap
        
    def compile(self, willExecutor):
        self.__project.findSources()
        self.__buildObjMap()
        self.__compileObjs(willExecutor)

    def resolveDependings(self, willExecutor):
        for dep in self.getProject().getDependences():
            dep.resolve(self, willExecutor)
            
    def buildBinary(self, willExecutor):
        self.__compiler.buildBinary(self, willExecutor, self.__goalFSItem)

    def buildWorkFlow(self, willExecutor):
        self.compile(willExecutor)
        self.resolveDependings(willExecutor)
        self.buildBinary(willExecutor)
        
    def getAllObjectItems(self, **params):
        result = []
        src2ObjMap = self.getSrc2ObjMap()
        for src in self.getProject().getSourceItems():
            if not self._skipObjectItem(src, **params):
                obj = src2ObjMap[src]
                result.append(obj)
	for dep in self.getProject().getDependences():
		result.extend(dep.getObjectItems())
        return result

    def getCompiler(self):
    	return self.__compiler

    def setAllocateObjStrategy(self, strat):
        self.__allocObjStrategy = strat

    def setGoalFSItem(self, goalFSItem):
        self.__goalFSItem = goalFSItem

    def setCompiler(self, compiler):
        self.__compiler = compiler
        
    def setBinDestFSItem(self, binDestFSItem):
        if binDestFSItem is None:
            binDestFSItem = FSItem(self.getProject().getRoot(), os.path.join("Out", "Bin"), self.getProject().getName())
        self.setGoalFSItem(binDestFSItem)

    def setDependenceBuildRoot(self, dependenceBuildRoot):
        self.__dependenceBuildRoot = dependenceBuildRoot

    def getDependenceBuildRoot(self):
        return self.__dependenceBuildRoot

    def _skipObjectItem(self, src, **params):
        return False
        
    def __buildObjMap(self):
        for src in self.__project.getSourceItems():
            obj = self.__allocObjStrategy.allocate(src)
            self.__src2objMap[src] = obj
            
    def __compileObjs(self, willExecutor):
        for src in self.__project.getSourceItems():
            self.__compiler.compile(src, self, willExecutor)
    
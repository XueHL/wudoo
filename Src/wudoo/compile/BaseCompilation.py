from wudoo.compile.ICompilation import ICompilation

class BaseCompilation(ICompilation):
    def __init__(self, project):
        self.__project = project
        
    def getProject(self):
        return self.__project
        
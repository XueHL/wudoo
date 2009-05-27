import os
from wudoo.compile.IPreCompileStrategy import IPreCompileStrategy

class CreateDestOnPreCompile(IPreCompileStrategy):
    def onPreCompile(self, objFSItem):
        self.__create(objFSItem)

    def onPreLink(self, objFSItem):
        self.__create(objFSItem)

    def __create(self, objFSItem):
        path = objFSItem.getPath()
        if not os.path.exists(path):
            try:
                os.makedirs(path);
            except:
                pass
            
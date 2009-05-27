class IPreCompileStrategy:
    def onPreCompile(self, objFSItem):
        raise NotImplementedError()
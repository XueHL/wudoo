import os
from wudoo.IWillExecutor import IWillExecutor

class SystemWillExecutor(IWillExecutor):
    def execute(self, cmd):
        os.system(cmd)

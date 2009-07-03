import subprocess
from wudoo.IWillExecutor import IWillExecutor

class SystemWillExecutor(IWillExecutor):
	def execute(self, cmd):
		#print cmd
		result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		#print result
		if self.__isErr(result):
			print result[1]

	def __isErr(self, stdErrOut):
		err = stdErrOut[1]
		if err is None:
			return False
		if len(err) == 0:
			return False
		if err.find("error") == -1:
			return False
		return True
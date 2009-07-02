import subprocess
from wudoo.IWillExecutor import IWillExecutor

class SystemWillExecutor(IWillExecutor):
	def execute(self, cmd):
		#print cmd
		result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		if self.__isErr(result):
			print result[0]

	def __isErr(self, stdErrOut):
		err = stdErrOut[0]
		if err is None:
			return False
		if len(err) == 0:
			return False
		return True
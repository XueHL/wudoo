import subprocess
from wudoo.IWillExecutor import IWillExecutor
from wudoo.IWillReportHandler import IWillReportHandler

class SystemWillExecutor(IWillExecutor, IWillReportHandler):
	def __init__(self, willReportHandler = None):
		if willReportHandler is None:
			willReportHandler = self
		self.__willReportHandler = willReportHandler
	
	def execute(self, cmd):
		result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		self.__willReportHandler.handleReport(result)
		
	def handleReport(self, result):
		if self.__isErr(result[1]):
			print result[1]

	def __isErr(self, errOut):
		if errOut is None:
			return False
		return errOut.find("erro") > 0

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
		self.__willReportHandler.handleReport(cmd, result)
		
	def handleReport(self, cmd, result):
		if self.__isErr(result[1]):
			print "CMD was:\n\t\t", cmd, "\nresult:\n\t\t", result[1]

	def __isErr(self, errOut):
		if errOut is None:
			return False
		if errOut.find("erro") > 0:
			return True
		if errOut.find("No such file") > 0:
			return True
		if errOut.find(".cpp") > 0:
			return True
		return False

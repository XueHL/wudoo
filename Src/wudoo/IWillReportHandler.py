class IWillReportHandler:
	def handleReport(self, cmd, result):
		raise NotImplementedError()
	
class NOPWillReportHandler(IWillReportHandler):
	def handleReport(self, cmd, result):
		pass
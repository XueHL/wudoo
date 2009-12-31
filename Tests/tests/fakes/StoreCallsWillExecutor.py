from wudoo.IWillExecutor import IWillExecutor

class StoreCallsWillExecutor(IWillExecutor):
	def __init__(self):
		self.history = []

	def execute(self, cmd):
		self.history.append(cmd)

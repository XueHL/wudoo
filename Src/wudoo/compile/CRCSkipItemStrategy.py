from wudoo.compile.ISkipItemsStrategy import ISkipItemsStrategy

class CRCSkipItemStrategy(ISkipItemsStrategy):
	def skip(self, srcFsItem, objFsItem):
		return False

	def onCompiled(self, srcFsItem, objFsItem):
		pass
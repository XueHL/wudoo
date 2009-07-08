class ISkipItemsStrategy:
	def skip(self, srcFsItem, objFsItem):
		raise NotImplementedError()

	def onCompiled(self, srcFsItem, objFsItem):
		raise NotImplementedError()
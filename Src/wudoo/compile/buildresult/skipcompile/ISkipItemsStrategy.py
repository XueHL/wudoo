class ISkipItemsStrategy:
	def skip(self, srcFsItem, compilation, project):
		raise NotImplementedError()

	def onCompiled(self, srcFsItem, compilation, project):
		raise NotImplementedError()
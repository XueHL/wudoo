class ISkipItemsStrategy:
	def skip(self, srcFsItem, objFsItem):
		raise NotImplementedError()
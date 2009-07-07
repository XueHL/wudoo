from wudoo.compile.ISkipItemsStrategy import ISkipItemsStrategy

class CompileAllStrategy(ISkipItemsStrategy):
	def skip(self, srcFsItem, objFsItem):
		return False

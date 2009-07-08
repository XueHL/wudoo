from wudoo.compile.buildresult.skipcompile.ISkipItemsStrategy import ISkipItemsStrategy

class CompileAllStrategy(ISkipItemsStrategy):
	def skip(self, srcFsItem, objFsItem):
		return False

	def onCompiled(self, srcFsItem, objFsItem):
		pass
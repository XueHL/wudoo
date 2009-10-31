from wudoo.compile.buildresult.skipcompile.ISkipItemsStrategy import ISkipItemsStrategy

class CompileAllStrategy(ISkipItemsStrategy):
	def skip(self, srcFsItem, compilation, project):
		return False

	def onCompiled(self, srcFsItem, compilation, project):
		pass
class IPreCompileStrategy:
	def onPreCompile(self, objFSItem):
		raise NotImplementedError()

	def onPreLink(self, objFSItem):
		raise NotImplementedError()
	
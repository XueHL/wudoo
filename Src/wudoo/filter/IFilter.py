class IFilter:
	def accepts(self, filePath):
		raise NotImplementedError()
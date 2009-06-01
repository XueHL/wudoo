from wudoo.filter.IFilter import IFilter

class AcceptAllFilter(IFilter):
	def accepts(self, filePath):
		return True	
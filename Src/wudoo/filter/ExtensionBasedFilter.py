import os
from wudoo.filter.IFilter import IFilter

class ExtensionBasedFilter(IFilter):
	def __init__(self, goodExts = {}):
		self.__goodExts = goodExts
		
	def accepts(self, filePath):
		ext = os.path.splitext(filePath)[1][1:]
		return self.__goodExts.has_key(ext)
		

from wudoo.FSItem import FSItem

class ArchiveFSItem(FSItem):
	"""\
Object item.
"""
	def __init__(self, *pathSteps):
		FSItem.__init__(self, *pathSteps)
from wudoo.FSItem import FSItem

class ObjectFSItem(FSItem):
	"""\
Object item.
"""
	def __init__(self, *pathSteps):
		FSItem.__init__(self, *pathSteps)
class IProjectSearcher:
	def searchProject(self, projectDescr):
		"""\
Returns IProject by projectDescr.
"""
		raise NotImplementedError()
	
class NOProjectSearch(IProjectSearcher):
	def searchProject(self, projectDescr):
		return projectDescr
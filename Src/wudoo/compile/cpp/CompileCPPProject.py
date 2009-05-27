from wudoo.compile.Project import Project
from wudoo.compile import SourceFilterColl 

class CompileCPPProject(Project):
	def __init__(self, rootPath = ""):
		Project.__init__(self, rootPath)
		self.setSourceFilter(SourceFilterColl.CPP_SOURCE_FILTER)

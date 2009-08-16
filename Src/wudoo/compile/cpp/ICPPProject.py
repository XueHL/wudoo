from wudoo.compile.IProject import IProject

class ICPPProject(IProject):
	def getHdrFolders(self):
		"""\
Returns header folders.
"""
		raise NotImplementedError()
	
	def getExportHdrFolders(self):
		"""\
Returns str[] - list of headers which user of the project have to  include.
"""
		raise NotImplementedError()
	
	def addHdrFolders(self, hdrFoldersDescr):
		"""\
Same as addSrcFolders but with headers.
"""
		raise NotImplementedError()
	
	def addExportHdrFolders(self, exportHhdrFoldersDescr):
		"""\
Same as addSrcFolders but with export headers.
"""
		raise NotImplementedError()

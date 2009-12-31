class IProject:
	"""\
Essence one can compile.
"""
	def getRoot(self):
		"""\
Returns project's root.
"""
		raise NotImplementedError()

	def getName(self):
		"""\
Returns project's name.
"""
		raise NotImplementedError()

	def getModuleFile(self):
		"""\
Returns str - file where the project was defined.
"""
		raise NotImplementedError()

	def getSourceItems(self):
		"""\
Returns FSItem[] - list of source items.
"""
		raise NotImplementedError()

	def getDependences(self):
		"""\
Returns IProject[] - list of dependences.
"""
		raise NotImplementedError()

	def addSrcFolders(self, sourceFoldersDescr):
		"""\
Adds source folders.
sourceFoldersDescr is a str[] => adds each element of sourceFoldersDescr OR
sourceFoldersDescr is a str then method works with sourceFoldersDescr.remove(" " || "\t").split("\n").  
"""
		raise NotImplementedError()
	
	def addDependenceProject(self, project):
		"""\
Adds dependence project.
"""
		raise NotImplementedError()

	def getSrcFolders(self):	
		"""\
Returns source folders.  
"""
		raise NotImplementedError()
		
	def isEntryPointObject(self, objFSItem):
		"""\
Returns true iff objFSItem is entry point.
"""
		raise NotImplementedError()

import pickle, os

class LibsRegOffice:
	def __init__(self, dbPath, modulesRegOffice):
		self.__dbPath = dbPath
		self.__modulesRegOffice = modulesRegOffice
		self.__name2modulepath = None
		self.__pairs = []
		self.__flushedCount = 0
	
	def registerLibrary(self, getProjectFunctor):
		projectInstance = getProjectFunctor()
		name = projectInstance.getName()
		moduleFile = projectInstance.getModuleFile()
		name2modulepath = self.__getName2modulepath()
		if name2modulepath.has_key(name) and name2modulepath[name] == moduleFile:
			return
		self.__add(name2modulepath, name, moduleFile)
		
	def libByName(self, name):
		name2modulepath = self.__getName2modulepath()
		if not name2modulepath.has_key(name):
			return None
		modulePath = name2modulepath[name]
		getProjectFunctor = self.__loadGetProjFunctor(modulePath)
		return getProjectFunctor()
		
	def flush(self):
		output = open(self.__dbPath, "a")
		for i in xrange(len(self.__pairs) - self.__flushedCount):
			j = i + self.__flushedCount
			pair = self.__pairs[j]
			pickle.dump(pair, output)
		output.close()
		
	def __getName2modulepath(self):
		if self.__name2modulepath is not None:
			return self.__name2modulepath
		self.__name2modulepath = {}
		input = None
		try:
			input = open(self.__dbPath, "r")
		except IOError:
			return self.__name2modulepath
		while True:
			pair = None
			try:
				pair = pickle.load(input)
			except EOFError:
				break
			if pair is None:
				break
			self.__add(self.__name2modulepath, pair[0], pair[1])
		self.__flushedCount = len(self.__pairs)
		return self.__name2modulepath
		
	def __add(self, name2modulepath, name, moduleFile):
		name2modulepath[name] = moduleFile
		self.__pairs.append((name, moduleFile))
		self.__modulesRegOffice.addDependProjDir(os.path.split(moduleFile)[0])
	
	def __loadGetProjFunctor(self, modulePath):
		moduleName = os.path.split(modulePath)[1]
		moduleName = os.path.splitext(moduleName)[0]
		MOD_NAME_2_GETTER = {}
		import build_er_lib
		MOD_NAME_2_GETTER["build_er_lib"] = build_er_lib.getProject
		return MOD_NAME_2_GETTER[moduleName]
	  
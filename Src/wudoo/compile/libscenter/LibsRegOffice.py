import pickle, os

class LibsRegOffice:
	def __init__(self, dbPath, modulesRegOffice):
		self.__dbPath = dbPath
		self.__modulesRegOffice = modulesRegOffice
		self.__name2modulepath = None
		self.__pairs = []
		self.__flushedCount = 0
		self.__localFoundModules = {}
	
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
		modulePath = None
		allDB = self.__mergeDicts(self.__localFoundModules, name2modulepath)
		if allDB.has_key(name):
			modulePath = allDB[name]
		
		if modulePath is not None:
			getProjectFunctor = self.__loadGetProjFunctor(modulePath)
			return getProjectFunctor()
		else:
			return name
		
	def setupArgsObj(self, argsObj, prjRoot):
		for searchArea in argsObj.developprojectssearch:
			searchArea = os.path.normpath(os.path.join(prjRoot, searchArea))
			self.__dfsModules(searchArea)
		
	def flush(self):
		output = open(self.__dbPath, "a")
		for i in xrange(len(self.__pairs) - self.__flushedCount):
			j = i + self.__flushedCount
			pair = self.__pairs[j]
			pickle.dump(pair, output)
		output.close()
		
	def __mergeDicts(self, *dicts):
		result = {}
		for d in dicts:
			for (k, v) in d.items():
				result[k] = v
		return result
		
	def __dfsModules(self, file):
		if os.path.isfile(file):
			ext = os.path.splitext(file)[1]
			if ext == ".py":
				try:
					functor = self.__loadGetProjFunctor(file)
					prj = functor()
					self.__localFoundModules[prj.getName()] = file
				except:
					pass
		else:
			for sub in os.listdir(file):
				sub = os.path.join(file, sub)
				self.__dfsModules(sub)
		
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
		modulePath = modulePath.replace(".pyc", ".py")
		moduleFileName = os.path.split(modulePath)[1]
		moduleName = os.path.splitext(moduleFileName)[0]
		import imp
		module = imp.load_module(moduleName, open(modulePath), modulePath, ("py", "U", imp.PY_SOURCE))
		return module.getProject
	  
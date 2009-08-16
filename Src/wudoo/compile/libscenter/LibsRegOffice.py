import pickle

class LibsRegOffice:
	def __init__(self, dbPath):
		self.__dbPath = dbPath
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
		name2modulepath[name] = moduleFile
		self.__pairs.append((name, moduleFile))
		
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
		input = open(self.__dbPath, "r")
		while True:
			pair = None
			try:
				pair = pickle.load(input)
			except EOFError:
				break
			if pair is None:
				break
			self.__name2modulepath[pair[0]] = pair[1]
			self.__pairs.append(pair)
		self.__flushedCount = len(self.__pairs)
		return self.__name2modulepath  
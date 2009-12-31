import os, imp

def runScript(*path):
	path = os.path.join(*path)
	module = imp.load_module(genName(), open(path), path, ("py", "U", imp.PY_SOURCE))

def genName():
	return "THE_NAME"
	
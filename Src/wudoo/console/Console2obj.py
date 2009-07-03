import sys

class Empty:
	pass

def argArr2obj(argv, *defaultsEmptyList):
	obj = Empty()
	dict = obj.__dict__

	for default in defaultsEmptyList:
		dict[default] = []

	top = None
	for it in argv:
		if it.find("--") > -1:
			it = it[2:]
			top = []
			dict[it] = top
		else:
			if top is not None:
				top.append(it)
	return obj

def consoleaArgs2obj(*args, **kwargs):
	return argArr2obj(sys.argv, *args, **kwargs)
import sys

class Empty:
	pass

def argArr2obj(argv, *defaultsEmptyList, **kwDefaults):
	obj = Empty()
	dict = obj.__dict__

	for default in defaultsEmptyList:
		dict[default] = []

	for k in kwDefaults.keys():
		dict[k] = kwDefaults[k]

	top = None
	bn = None
	for it in argv:
		if it.find("--") > -1:
			it = it[2:]
			top = []
			dict[it] = top
		elif it.find("-b-") > -1:
			it = it[3:]
			bn = it
			top = None
			dict[it] = top
		else:
			if bn:
				dict[bn] = (it == "True")
			if top is not None:
				top.append(it)
	return obj

def consoleaArgs2obj(*args, **kwargs):
	return argArr2obj(sys.argv, *args, **kwargs)
import sys

class EmptyObj:
	pass

def argArr2obj(argv, obj = None):
	if obj is None:
		obj = EmptyObj()
	dict = obj.__dict__

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

def consoleaArgs2obj(obj = None):
	return argArr2obj(sys.argv, obj)
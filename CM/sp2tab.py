import os, sys

def rec(p):
	if p.find(".svn") > -1:
		return
	if os.path.isfile(p):
		ext = os.path.splitext(p)[1]
		if ext == ".py":
			b = open(p, "r").read()
			binit = b
			b = b.replace("	", "\t")
			if (binit != b):
				print p
				f = open(p, "w")
				f.write(b)
				f.close()
	else:
		for s in os.listdir(p):
			sp = os.path.join(p, s)
			rec(sp)

p = sys.path[0]
p = os.path.split(p)[0]
rec(p)
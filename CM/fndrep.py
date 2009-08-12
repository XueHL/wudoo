import os, sys

SRC = "StoreCompilationPool"
GOAL = "StoreCompilationPool"

def rec(p):
	if p.find(".svn") > -1:
		return
	if os.path.isfile(p):
		ext = os.path.splitext(p)[1]
		if ext == ".py" and p != "fndrep.py":
			b = open(p, "r").read()
			binit = b
			b = b.replace(SRC, GOAL)
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

for cl in ["IConneryExperimentContext", "ConneryExperimentContext"]:
	cl = os.path.splitext(cl)[0]
	SRC = "jeconbond.experiment.natural.prodpossibfrontier.process." + cl
	GOAL = "jeconbond.experiment.natural.prodpossibfrontier.process." + cl
	#rec(p)

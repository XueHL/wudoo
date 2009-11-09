import os, sys

SRC = "import org.apache.xml.serialize.XMLSerializer;"
GOAL = "import com.sun.org.apache.xml.internal.serialize.XMLSerializer;"

def rec(p):
	if p.find(".svn") > -1:
		return
	if os.path.isfile(p):
		ext = os.path.splitext(p)[1]
		if ext == ".java":
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

rec("cpptasks-1.0b5")

SRC = "import org.apache.xml.serialize.OutputFormat;"
GOAL = "import com.sun.org.apache.xml.internal.serialize.OutputFormat;"
rec("cpptasks-1.0b5")

SRC = "import org.apache.xml.serialize.Serializer;"
GOAL = "import com.sun.org.apache.xml.internal.serialize.Serializer;"
rec("cpptasks-1.0b5")

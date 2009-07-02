import subprocess, os, sys

cmd = "g++ " + \
	" -c " + \
	" *.cpp " + \
	" -g3 " + \
	" -O0 " + \
	""
ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"

def hellolib():
	shared = len(sys.argv) > 0 and "shared" in sys.argv
	if shared:
		cmd = "g++ " + \
			" -shared " + \
			" Hello.o " + \
			" -o " + \
			" Hello.dll " + \
			""
		ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"
		return "Hello.dll"
	else:
		cmd = "ar " + \
			" q " + \
			" Hello.a " + \
			" Hello.o " + \
			""
		ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"
		return "Hello.a"

libn = hellolib()

cmd = "g++ " + \
	" Main.o " + \
	libn + \
	" -o " + \
	" Hello-debug " + \
	""
ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"

def rm(n):
	if os.path.exists(n):
		os.remove(n)
rm("Hello.o")
rm("Hello.a")
rm("Main.o")

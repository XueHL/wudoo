import subprocess, os

cmd = "g++ " + \
	" -c " + \
	" *.cpp " + \
	" -g3 " + \
	" -O0 " + \
	""
ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"

cmd = "ar " + \
	" q " + \
	" Hello.a " + \
	" Hello.o " + \
	""
ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"

cmd = "g++ " + \
	" Main.o " + \
	" Hello.a " + \
	" -o " + \
	" Hello-debug " + \
	""
ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
print "###\n\n", str(ret).replace("\n", "\n\t\t"), "\n\n###\n"

os.remove("Hello.o")
os.remove("Hello.a")
os.remove("Main.o")

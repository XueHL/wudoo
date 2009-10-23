import sys, os
sys.path.append(os.path.abspath(os.path.join("..", "Outer", "SufString", "CM")))

from wudoo.compile.cpp.Front import *
import sufstring
LIBS_REG_OFFICE.registerLibrary(sufstring.getProject)

import ause

auseProject = ause.getProject()

wdefaultBuild(auseProject)

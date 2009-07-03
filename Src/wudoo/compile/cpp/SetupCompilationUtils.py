import os

from wudoo.compile.allocate.OutputRootBasedAllocate import OutputRootBasedAllocate

def setupPathsFromRoot(compilation, project, root = None):
	if root is None:
		root = os.path.join(project.getRoot(), "Out")
	allocStrat = OutputRootBasedAllocate(
		root = root,
		objFolder = "Obj",
		objExt = ".o",
		binFolder = "Bin",
		outerFolder = "Outer",
		rootProject = project
		)
	compilation.setAllocateStrategy(allocStrat)

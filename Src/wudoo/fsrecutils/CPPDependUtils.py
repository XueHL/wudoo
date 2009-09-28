import os
from wudoo.FSItem import FSItem
from wudoo.compile.libscenter.IProjectSearcher import *
from wudoo.compile.IProject import IProject

def getAllHeadersByProject(project):
	result = []
	appendHeaderFolders(project.getHdrFolders(), project, result)
	for depPrj in getAllDependProjects(project, True):
		appendHeaderFolders(depPrj.getExportHdrFolders(), depPrj, result)
	return result

def appendHeaderFolders(folderList, project, dest):
	for hdr in folderList:
		dest.append(os.path.join(project.getRoot(), hdr))

def getAllDependProjects(project, includeTheProject = False):
	dest = []
	dfs_getAllDependProjects(project, dest)
	if includeTheProject:
		dest.append(project)
	return dest

def dfs_getAllDependProjects(project, dest):
	for depPrj in project.getDependences():
		dest.append(depPrj)
		dfs_getAllDependProjects(depPrj, dest)

def getFilteredFiles(rootPath, folderList, filter):
	dest = []
	for srcFold in folderList:
		dfs_getFilteredFiles(rootPath, srcFold, "", filter, dest)
	return dest

def dfs_getFilteredFiles(rootPath, srcFold, cur, filter, dest):
	curGl = os.path.join(rootPath, srcFold, cur)
	if os.path.isfile(curGl):
		if filter.accepts(curGl):
			dest.append(FSItem(rootPath, srcFold, cur))
	else:
		for sub in os.listdir(curGl):
			curPr = os.path.join(cur, sub)
			dfs_getFilteredFiles(rootPath, srcFold, curPr, filter, dest)

def getDependHeaders(project):
	dest = []
	return dest

def substituteAllProjects(project, projectSearcher):
	"""\
projectSearcher is a IProjectSearcher.
"""
	depPrjDescr = project.getDependences()
	n = len(depPrjDescr)
	for i in xrange(n):
		prjdescr = depPrjDescr[i]
		prj = projectSearcher.searchProject(prjdescr)
		if not isinstance(prj, IProject):
			raise "Can't find: " + str(prjdescr)
		depPrjDescr[i] = prj
		substituteAllProjects(prj, projectSearcher)

import os
from wudoo.FSItem import FSItem

def getAllHeadersByProject(project):
	result = []
	appendHeaderFolders(project.getHdrFolders(), project, result)
	for depPrj in getAllDependProjects(project):
		appendHeaderFolders(depPrj.getExportHdrFolders(), depPrj, result)
	return result

def appendHeaderFolders(folderList, project, dest):
	for hdr in folderList:
		dest.append(os.path.join(project.getRoot(), hdr))

def getAllDependProjects(project):
	dest = []
	dfs_getAllDependProjects(project, dest)
	return dest

def dfs_getAllDependProjects(project, dest):
	dest.append(project)
	for depPrj in project.getDependences():
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
import os

def getAllHeadersByProject(project):
	result = []
	appendHeaderFolders(project.getHdrFolders(), project, result)
	dfs_getAllHeadersByProject(project, result)
	return result

def dfs_getAllHeadersByProject(project, dest):
	appendHeaderFolders(project.getExportHdrFolders(), project, dest)
	for depPrj in project.getDependences():
		dfs_getAllHeadersByProject(depPrj, dest)

def appendHeaderFolders(folderList, project, dest):
	for hdr in folderList:
		dest.append(os.path.join(project.getRoot(), hdr))
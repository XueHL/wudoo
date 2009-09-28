from wudoo.modulesutils.FileAsModuleUtils import *

DOC_STORRAGE = {}

def getTextProc(docName, the__file__):
	"""
docName - str identifyer
the__file__ == __file__ see Examples\TextProc\000-trivial-text-aligm\TheLordOfTheRings.py
"""	
	if DOC_STORRAGE.has_key(docName):
		return DOC_STORRAGE[docName]
	else:
		from wudoo.textproc.processing.TextProcessor import TextProcessor
		result = TextProcessor(docName, the__file__)
		DOC_STORRAGE[docName] = result
		return result

from wudoo.textproc.processing.IToolsOperationStraegy import IToolsOperationStraegy

class DefaultToolsOperationStraegy(IToolsOperationStraegy):
	def appendTool(self, toolsList, newTool):
		n = len(toolsList)
		top = toolsList[n - 1]
		top.dispose()
		toolsList.append(newTool)
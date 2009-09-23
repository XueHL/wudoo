class IElement:
	def visit(self, visitor):
		raise NotImplementedError(self.__class__)
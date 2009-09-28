class IResolveDependenceStrategy:
	def resolve(self, depPrj, parentCompilation, willExecutor):
		raise NotImplementedError()

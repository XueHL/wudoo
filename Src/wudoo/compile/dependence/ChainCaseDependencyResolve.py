from wudoo.compile.dependence.IResolveDependenceStrategy import IResolveDependenceStrategy

class UseDefaultStageFunctor:
	def __init__(self, defaultResolveDependenceStrategy):
		self.__defaultResolveDependenceStrategy = defaultResolveDependenceStrategy
	def __call__(self, project):
		return self.__defaultResolveDependenceStrategy

class ChainCaseDependencyResolve(IResolveDependenceStrategy):
	def __init__(self, defaultStrategy):
		self.__stages = []
		self.addStage(UseDefaultStageFunctor(defaultStrategy))

	def addStage(self, chooseStrategyStageFunctor):
		self.__stages = [chooseStrategyStageFunctor] + self.__stages

	def resolve(self, depPrj, parentCompilation, willExecutor):
		for stageFunctor in self.__stages:
			strategy = stageFunctor(depPrj)
			if strategy is not None:
				return strategy.resolve(depPrj, parentCompilation, willExecutor)
		raise NotImplementedError()	
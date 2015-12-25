import scipy.optimize
class ols(object):
	"""
	Return OLS(Ordinary Least Square) optimized parameters.
	"""

	def __init__(self, model, cost_func):
		self.model = model
		self.cost_func = cost_func

	def estimate(self):
		pass

def gls():
	"""
	Return GLS(Generalized Least Square) optimized parameters.
	"""
	print "Hello, World!"

if __name__ == '__main__':
	from ...models import *
	ols = ols(None, None)
	print ols
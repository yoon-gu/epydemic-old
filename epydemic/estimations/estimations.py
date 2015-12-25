import scipy.optimize
class ols(object):
	"""
	Return OLS(Ordinary Least Square) optimized parameters.
	"""

	def __init__(self, model, cost_func):
		self.model = model
		self.cost_func = cost_func

	def estimate(self, initial_value, Y):
		L = self.cost_func
		theta0 = initial_value
		theta_ols = scipy.optimize.fmin(func=L, x0=theta0, args=(Y,))
		self.estimated = theta_ols
		return theta_ols

def gls():
	"""
	Return GLS(Generalized Least Square) optimized parameters.
	"""
	print "Hello, World!"

if __name__ == '__main__':
	from ...models import *
	ols = ols(None, None)
	print ols
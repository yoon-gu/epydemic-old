"""
Epydemic Module
===============

``epydemic`` is a software package written in ``Python`` for mathematical epidemic modeling. There are three submodules.

* ``models`` contains epidemic modeling ordinary differential equation(ODE).
* ``estimations`` performs parameter estimations given real world data.
* ``controls`` solves optimal a control problem.

Example
-------
Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks.

	$ python example_numpy.py


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented.

Notes
-----
	This is an example of an indented section. It's like any other section,
	but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created simply by
resuming unindented text.

"""
__author__ = ("Jacob Hwang <jacob@dnry.org>")

__all__ = ["models", "estimations", "epydemic_app"]

import models, estimations#, epydemic_app

if __name__ == '__main__':
	from numpy.random import randn
	from numpy import array
	# parameters for each model
	beta = 5e-6
	gamma = 5e-1
	S0 = 3.5e5
	I0 = 9e1
	R0 = 0.
	dt = 1
	start = 0
	end = 10

	parameter = {'beta' : beta, 'gamma' : gamma, 'dt':dt, 'start':start, 'end':end}

	# initial values for each model
	S0, I0, R0 = 1.0 - 1.0e-6, 1.0e-6, 0.0
	Initial = (S0, I0, R0)

	md = models.sir()
	md.set_parameters(parameter)
	md.set_initial_values(Initial)

	# Solve Ordinary Differential Equation
	dt = parameter['dt']
	beta = parameter['beta']

	sol = md.solve()
	print sol
	S, I = sol[:,0], sol[:,1]
	SI = S * I
	Z = 0.5 * dt * beta * ( SI[:-1] + SI[1:] )

	# Adding Noise
	alpha = 0.5
	c = alpha * min(Z)
	print len(Z)
	Y = Z + c * randn(len(Z))

	# Getting noisy parameter, intentionally
	theta = array([S0,I0,beta,gamma])
	theta0 = 1.25 * theta

	# Estimating parameter
	sir = md.diff_eqs
	def L(theta, Y):
		from numpy import linspace
		from scipy.integrate import odeint
		from numpy import linalg as LA
		n = 1000
		initial = (theta[0], theta[1], 0.)
		timep = linspace(0, 14, n+1)
		sol = odeint(sir, initial, timep,
			args = ({'beta':theta[2], 'gamma':theta[3]}, ))
		S, I = sol[:,0], sol[:,1]
		SI = S * I
		Z = 0.5 * ( timep[1:] - timep[:-1] ) * beta * ( SI[:-1] + SI[1:] )
		return LA.norm(Z - Y)

	est = estimations.ols(md, L)
	print est.estimate(theta0, Y)
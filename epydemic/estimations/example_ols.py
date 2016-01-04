from numpy import array, arange, zeros, linspace
from scipy.integrate import odeint
from numpy.random import randn
import scipy.optimize
from numpy import linalg as LA

# Parameters
beta = 5e-6
gamma = 5e-1
S0 = 3.5e5
I0 = 9e1
R0 = 0.
theta = array([S0,I0,beta,gamma])

# Discrete Time Domain
t_start = 0
t_end = 14
t_inc = 0.5
t_range = arange(t_start, t_end + t_inc, t_inc)

# SIR Model
def sir(INP, t, params):
    beta = params['beta']
    gamma = params['gamma']
    Y = zeros((3))
    V = INP
    Y[0] = - beta * V[0] * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y # For odeint

# Solve Ordinary Differential Equation
sol = odeint(sir, (S0, I0, R0), t_range,
    args = ({'beta':beta, 'gamma':gamma}, ))

S, I = sol[:,0], sol[:,1]
SI = S * I
Z = 0.5 * t_inc * beta * ( SI[:-1] + SI[1:] )

# Adding Noise
alpha = 0.5
c = alpha * min(Z)
Y = Z + c * randn(len(Z))

# Getting noisy parameter, intentionally
theta0 = 1.25 * theta

# Estimating parameter
def L(theta, timep, Y):
    initial = (theta[0], theta[1], 0.)
    sol = odeint(sir, initial, t_range,
        args = ({'beta':theta[2], 'gamma':theta[3]}, ))
    S, I = sol[:,0], sol[:,1]
    SI = S * I
    Z = 0.5 * ( t_range[1:] - t_range[:-1] ) * beta * ( SI[:-1] + SI[1:] )
    return LA.norm(Z - Y)

theta_ols = scipy.optimize.fmin(func=L, x0=theta0, args=(t_range, Y,))

print theta_ols
from numpy import array, arange, zeros, linspace
from scipy.integrate import odeint
from numpy.random import randn
import scipy.optimize
from numpy import linalg as LA

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

def ols_cost(theta, timep, Y):
    initial = (theta[0], theta[1], 0.)
    sol = odeint(sir, initial, t_range,
        args = ({'beta':theta[2], 'gamma':theta[3]}, ))
    S, I = sol[:,0], sol[:,1]
    SI = S * I
    Z = 0.5 * ( t_range[1:] - t_range[:-1] ) * beta * ( SI[:-1] + SI[1:] )
    return LA.norm(Z - Y)

# Parameters
beta = 5e-6
gamma = 5e-1
S0 = 3.5e5
I0 = 9e1
R0 = 0.
t_start = 0
t_end = 14
t_inc = 0.014
t_range = arange(t_start, t_end + t_inc, t_inc)

parameter = {
        'beta' : beta, 
        'gamma' : gamma, 
        'S0' : S0, 
        'I0' : I0,
        'R0' : R0, 
        't_range' : t_range, 
        }

# Solve Ordinary Differential Equation
sol = odeint(sir, (S0, I0, R0), t_range,
    args = (parameter, ))

S, I = sol[:,0], sol[:,1]
SI = S * I
Z = 0.5 * t_inc * beta * ( SI[:-1] + SI[1:] )

# Adding Noise
alpha = 0.5
c = alpha * min(Z)
Y = Z + c * randn(len(Z))

# Getting noisy parameter, intentionally
theta = array([S0,I0,beta,gamma])
theta0 = 1.25 * theta

# Estimating parameter
theta_ols = scipy.optimize.fmin(func=ols_cost, x0=theta0, args=(t_range, Y,))

print theta_ols

import matplotlib.pyplot as plt
S, I = sol[:,0], sol[:,1]
SI = S * I
beta = theta_ols[2]
incidence = 0.5 * t_inc * beta * ( SI[:-1] + SI[1:] )
plt.plot(t_range[:-1], Y, 's', color='gray')
plt.plot(t_range[:-1], incidence, 'k')
plt.ylabel('Number of cases')
plt.xlabel('Time')

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(incidence, (Y-incidence) / incidence, 'o')
ax1.set_xlabel('Model')
ax1.set_ylabel('Residual')
ax2.plot(t_range[:-1], (Y-incidence) / incidence, 'o')
ax2.set_xlabel('Time')
ax2.set_ylabel('Residual')
plt.ylim(ymax=50, ymin=-50)
plt.show()
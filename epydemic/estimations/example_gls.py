from numpy import array, arange, zeros, linspace, ones, dot, abs, sum
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

def gls_cost(theta, timep, Y, weight):
    initial = (theta[0], theta[1], 0.)
    sol = odeint(sir, initial, t_range,
        args = ({'beta':theta[2], 'gamma':theta[3]}, ))
    S, I = sol[:,0], sol[:,1]
    SI = S * I
    Z = 0.5 * ( t_range[1:] - t_range[:-1] ) * beta * ( SI[:-1] + SI[1:] )
    return dot(Z - Y, weight * (Z - Y))

def compute_zw(parameter, sir):
    beta = parameter['beta']
    t_range = parameter['t_range']
    S0 = parameter['S0']
    I0 = parameter['I0']
    R0 = parameter['R0']
    sol = odeint(sir, (S0, I0, R0), t_range, args = (parameter,))
    S, I = sol[:,0], sol[:,1]
    SI = S * I
    Z = 0.5 * (t_range[1:] - t_range[:-1]) * beta * ( SI[:-1] + SI[1:] )
    weight = 1. / Z**2
    return Z, weight

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
        'beta' : 5e-6, 
        'gamma' : 5e-1, 
        'S0' : 3.5e5, 
        'I0' : 9e1, 
        'R0' : 0., 
        't_range' : t_range, 
        }

# Solve Ordinary Differential Equation
sol = odeint(sir, (S0, I0, R0), t_range, args = (parameter,))

S, I = sol[:,0], sol[:,1]
SI = S * I
Z = 0.5 * t_inc * beta * ( SI[:-1] + SI[1:] )

# Adding Noise
alpha= 0.075
Y = Z * (ones(len(Z)) + alpha * randn(len(Z)))

# Getting noisy parameter, intentionally
theta = array([S0,I0,beta,gamma])
theta0 = 1.1 * theta

theta_ols = scipy.optimize.fmin(func=ols_cost, x0=theta0, args=(t_range, Y,))

Z, weight = compute_zw(parameter, sir)

# Loop
tol = 1e-5
maxit_out = 100
itcnt_out = 0
test = -1
theta_gls = theta_ols
while (itcnt_out < maxit_out) and (test < 0):
    itcnt_out += 1
    theta_est = theta_gls

    theta_gls = scipy.optimize.fmin(func=gls_cost, x0=theta_gls, args=(t_range, Y, weight))
    parameter['S0'] = theta_gls[0]
    parameter['I0'] = theta_gls[1]
    parameter['beta'] = theta_gls[2]
    parameter['gamma'] = theta_gls[3]
    Z, weight = compute_zw(parameter, sir)

    print itcnt_out, theta_gls

    temp = [tol * sum(abs(theta_gls[0])) - sum(abs(theta_est[0] - theta_gls[0])), 
            tol * sum(abs(theta_gls[1])) - sum(abs(theta_est[1] - theta_gls[1])), 
            tol * sum(abs(theta_gls[2])) - sum(abs(theta_est[2] - theta_gls[2])), 
            tol * sum(abs(theta_gls[3])) - sum(abs(theta_est[3] - theta_gls[3])), ]
    test = min(temp)

import matplotlib.pyplot as plt
S, I = sol[:,0], sol[:,1]
SI = S * I
beta = theta_gls[2]
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

plt.figure()
R_gls = theta_gls[2] * S / theta_gls[3]
plt.plot(t_range, R_gls, 'k')
plt.xlabel('Time')
plt.ylabel('R(t) Sample')
plt.show()

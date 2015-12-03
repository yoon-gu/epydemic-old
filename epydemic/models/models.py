def seir(gamma = 0.1, beta = 0.5, mu = 0.2, a = 1):
    r"""
    SEIR Model:

    .. math::
        :nowrap:

        \begin{align*}
            S' &= \mu N - \mu S - \beta \frac{I}{N} S \\
            E' &= \beta \frac{I}{N} S - (\mu +a ) E \\
            I' &= a E - (\gamma +\mu ) I \\
            R' &= \gamma I  - \mu R
        \end{align*}

    Parameters
    ----------
    gamma : float
        Description of gamma
    beta : float
        Description of beta
    mu : float
        Description of mu
    a : float
        Description of a

    Returns
    -------
    bool
        Description of return value

    """
    print "SEIR Model"

from scipy.integrate import odeint
from numpy import arange, zeros

class model(object):
    r"""
    This is just a quick example for a model.

    Example
    -------
    loem

    Parameters
    ----------
    gamma : float
        Description of gamma
    beta : float
        Description of beta
    mu : float
        Description of mu
    a : float
        Description of a

    Returns
    -------
    bool
        Description of return value
    """

    def __init__(self, eqn):
        self.equation = eqn

    def __str__(self):
        return "Hello"

    def set_parameters(self, param):
        self.parameter = param

    def set_initial_values(self, init_val):
        self.initial_value = init_val

    def solve(self):
        # solve model
        t_start = 0.0; t_end = 10; t_inc = 1
        t_range = arange(t_start, t_end + t_inc, t_inc)
        self.sol = odeint(self.equation, self.initial_value, t_range, args = (self.parameter, ))
        return self.sol

class sir(model):
    r"""
    SIR model:

    .. math::
        :nowrap:

        \begin{align*}
            S' &= -\beta S I \\
            I' &= \beta S I - \gamma I \\
            R' &= \gamma I
        \end{align*}

    Args:
        gamma (float): Description of gamma
        beta (float): Description of beta

    Example
    -------

        # parameters for each model
        parameter = {'beta' : 1.42, 'gamma' : 0.143}

        # initial values for each model
        S0, I0, R0 = 1.0 - 1.0e-6, 1.0e-6, 0.0
        Initial = (S0, I0, R0)

        # time range(step, end)
        TS, ND = 1, 10

        md = sir()
        md.set_parameters(parameter)
        md.set_initial_values(Initial)
        print md.solve()

        [[  9.99999000e-01   1.00000000e-06   0.00000000e+00]
         [  9.99996073e-01   3.63212714e-06   2.94749605e-07]
         [  9.99985620e-01   1.30325401e-05   1.34743012e-06]
         [  9.99948106e-01   4.67687249e-05   5.12538893e-06]
         [  9.99813542e-01   1.67779443e-04   1.86781170e-05]
         [  9.99331347e-01   6.01394782e-04   6.72579995e-05]
         [  9.97606329e-01   2.15242978e-03   2.41241135e-04]
         [  9.91471983e-01   7.66562607e-03   8.62390529e-04]
         [  9.70115005e-01   2.68296531e-02   3.05534209e-03]
         [  9.00912671e-01   8.85792322e-02   1.05080964e-02]
         [  7.20118903e-01   2.46816064e-01   3.30650331e-02]]
    """

    def diff_eqs(self, INP, t, params):
        from numpy import arange, zeros
        beta = params['beta']
        gamma = params['gamma']
        Y = zeros((3))
        V = INP
        Y[0] = - beta * V[0] * V[1]
        Y[1] = beta * V[0] * V[1] - gamma * V[1]
        Y[2] = gamma * V[1]
        return Y   # For odeint

    def __init__(self):
        super(sir, self).__init__(self.diff_eqs)
        

if __name__ == '__main__':
    # parameters for each model
    parameter = {'beta' : 1.42, 'gamma' : 0.143}

    # initial values for each model
    S0, I0, R0 = 1.0 - 1.0e-6, 1.0e-6, 0.0
    Initial = (S0, I0, R0)

    # time range(step, end)
    TS, ND = 1, 10

    md = sir()
    md.set_parameters(parameter)
    md.set_initial_values(Initial)
    print md.solve()

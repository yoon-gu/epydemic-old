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

def sir(gamma = 0.1, beta = 0.5):
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
	    gamma (float): Description of :math: \gamma
	    beta (float): Description of beta
	
	Example
	-------
	This is just a quick example.
	"""
	print "SIR Model"

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
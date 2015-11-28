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
	"""
	print "SIR Model"

def seir(gamma = 0.1, beta = 0.5, mu = 0.2):
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
	"""
	print "SEIR Model"
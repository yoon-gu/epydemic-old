from numpy import genfromtxt, arange, vstack, hstack, array, diag

S_0 = 98.798
I_0 = 0.0020091
beta = 0.0024581
gamma = 0.14286

D_perc_SIR = genfromtxt('D_perc_SIR.csv')
Dv = vstack((arange(1, 251), D_perc_SIR[6:256]))

# exp setting
p = 1.10
rate = 0.10

# number of seed 
N1 = 100
N2 = 1

# initial guess
ini_mean = array([S_0, I_0, p*beta, gamma])
ini_cov = diag((rate * ini_mean * (rate*ini_mean < 1) + (rate*ini_mean >= 1))**2)

# rate * ini_mean .* (rate*ini_mean < 1) + (rate*ini_mean >= 1)
# ini_cov = diag((rate*ini_mean.*(rate*ini_mean<1)+(rate*ini_mean>=1)).^2)
initial_guess = hstack((ini_mean.reshape(4,1), ini_cov))
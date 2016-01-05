from numpy import genfromtxt, arange, vstack, hstack, array, diag, zeros

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

Data = Dv
Initial_guess = initial_guess

# EKF function
# numerical decision
Ndt = 50 # uniform division number bet. each data

# manipulate input to fit my algorithm
t_z = Data[0, :] 
z = Data[1:,:] # data
x_0 = Initial_guess[:,0]
P_0 = Initial_guess[:,1:] # initial guess
Nd = len(t_z) # number of data
Dynamics_dim = len(x_0)
Measurement_dim = z.shape[0]

# start EKF
xhat = zeros((Dynamics_dim,Nd))
xhatP = zeros((Dynamics_dim,Nd))
xhat_ = x_0
P_ = P_0

for i in xrange(0,Nd):
	if i == 0:
		dt = t_z[0] / Ndt;
	else:
		dt = (t_z[i] - t_z[i-1]) / Ndt;

# for i = 1:Nd
#     if i == 1
#         dt = t_z(1)/Ndt;
#     else
#         dt = (t_z(i)-t_z(i-1))/Ndt;
#     end
    
#     for j = 1:Ndt
#         X = [xhat_ P_];
#         X = myODE(@(Y) MathcalF_E(Y,dt),dt,X); 
#         xhat_ = X(:,1);
#         P_ = X(:,2:end);
#     end
#     xhatP(:,i) = xhat_;
# %     update x; xhat
#     K = ((ME_R(xhat_)'+ME_H1(xhat_)*P_'*ME_H1(xhat_)')\...
#         (ME_H1(xhat_)*P_'))';
#     xhat(:,i) = xhat_ + K*(z(i) - ME_h(xhat_));
#     P_ = (eye(Dynamics_dim)-K*ME_H1(xhat_))*P_;
#     xhat_ = xhat(:,i);
# end
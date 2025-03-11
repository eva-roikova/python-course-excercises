import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# Loading of the data
exp_data = np.load("I_q_IPA_exp.npy")
model_data = np.load("I_q_IPA_model.npy")

# Experimental data
s_exp = exp_data[:,0] #scattering vector
I_s_exp = exp_data[:,1] #scattering strength
# Model data
s_model = model_data[:,0] #scattering vector
I_s_model = model_data[:,1] #scattering strength

# Theoretical model interpolation
interp_model = interp1d(s_model, I_s_model, kind="linear", fill_value="extrapolate")

# Interpolated values for the experimental scattering vector values
I_model_interp = interp_model(s_exp)

# Least-squares fitting
def loss_function(scaling_factor):
    return np.sum((I_s_exp - scaling_factor * I_model_interp) ** 2)

# Use minimize_scalar
result = minimize_scalar(loss_function, bounds=(0, 3e-4), method='bounded')
optimal_s= result.x
print("Optimal scaling factor (numerical):", optimal_s)

# Scaled theoretical intensity
I_model_scaled = optimal_s * I_model_interp

# Plot the experimental and scaled theoretical data
plt.figure(4)
plt.scatter(s_exp, I_s_exp, label="Experimental Data")
print(np.size(s_exp))
print(np.size(I_model_interp))
plt.plot(s_exp, I_model_scaled, label="Scaled Theoretical Model", color="red", linestyle="--")
plt.xlabel("Scattering Vector (s)")
plt.ylabel("Scattering Strength (I_s)")
plt.legend()
plt.title("Best Fit of Theoretical Model to Experimental Data")
plt.show()


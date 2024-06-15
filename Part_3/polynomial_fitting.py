import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the measured times
data = pd.read_csv('results/complexity_results.csv')
n_values = data['n']
times_t0 = data['Time_t0']
times_t1 = data['Time_t1']

# Fit polynomials to the measured times
poly_fit_t0 = np.polyfit(n_values, times_t0, 2)
poly_fit_t1 = np.polyfit(n_values, times_t1, 3)

# Generate polynomial values for plotting
poly_vals_t0 = np.polyval(poly_fit_t0, n_values)
poly_vals_t1 = np.polyval(poly_fit_t1, n_values)

# Plotting the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values, times_t0, label='Measured t0', color='blue')
plt.plot(n_values, poly_vals_t0, label='Polynomial fit t0', color='red')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Complexity of function_t0')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_values, times_t1, label='Measured t1', color='blue')
plt.plot(n_values, poly_vals_t1, label='Polynomial fit t1', color='red')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Complexity of function_t1')
plt.legend()

plt.tight_layout()
plt.savefig('results/complexity_analysis.png')
plt.show()

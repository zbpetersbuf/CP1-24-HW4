"""
This module performs a linear fit on grouped data from grouped_data_filtered.csv
and generates a plot displaying the data points with error bars and the best-fit line.
It imports the necessary libraries, including functions from `linear_fit.py` and loads
the filtered grouped data from the csv file. It performs a weighted least-squares linear fit
using uncertainties in `v`. Finally, it plots the grouped data with error bars and overlays the
best-fit line.

Dependencies:
- `linear_fit.py`: This script requires the `linear_fit` and `read_data_from_csv` functions.
- `grouped_data_filtered.csv`: The filtered data output file produced by the
`grouped_data_generator.py` script.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from linear_fit import linear_fit, read_data_from_csv

# Path to the filtered CSV file created by grouped_data_generator.py
csv_file_path = 'Least-squares Fit/grouped_data_filtered.csv'

# Use read_data_from_csv function to load the filtered data
x, y, sigma = read_data_from_csv(csv_file_path)

# Perform the linear fit using linear_fit function
fit_results = linear_fit(x, y, sigma)
print(fit_results)

# Generate plot with fit line and parameters
x_fit = np.linspace(min(x), max(x), 100)
y_fit = fit_results['intercept'] + fit_results['slope'] * x_fit

plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=sigma, fmt='o', color='purple', label='Grouped Data with Uncertainties')
plt.plot(x_fit, y_fit, color='red', label=f'Best Fit Line: v = {fit_results["intercept"]:.2f} + {fit_results["slope"]:.2f}*r')
plt.xlabel('r ($10^6$ parsecs)')
plt.ylabel('v (km/s)')
plt.title('Grouped Data with Least-Squares Fit')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
